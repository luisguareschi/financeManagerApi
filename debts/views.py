from django.db.models import Sum
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from debts.models import Debt, Debtor
from debts.serializers import DebtSerializer


# Create your views here.


class DebtsViewSet(viewsets.ModelViewSet):
    serializer_class = DebtSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        return Debt.objects.filter(user=self.request.user).order_by('-created')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def summary(self, request):
        queryset = self.get_queryset()

        total = queryset.aggregate(total=Sum('amount'))['total']
        last_updated = queryset.first().created if queryset.exists() else None

        response = {
            'total': total if total else 0,
            "last_updated": last_updated,
        }

        user_debtors = Debtor.objects.filter(created_by=request.user)
        debtors = []
        for debtor in user_debtors:
            debtors.append({
                'id': debtor.id,
                'name': debtor.name,
                'total': debtor.total_debt,
                'last_updated': debtor.last_updated,
            })

        # ordern users_debtors by total debt
        debtors = sorted(debtors, key=lambda x: x['total'], reverse=True)

        response['debtors'] = debtors

        return Response(response, status=200)
