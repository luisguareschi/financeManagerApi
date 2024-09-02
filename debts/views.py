from django.db.models import Sum
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from debts.models import Debt, Debtor
from debts.serializers import DebtSerializer, DebtorSerializer, CreateDebtSerializer


# Create your views here.


class DebtsViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateDebtSerializer
        return DebtSerializer

    def get_queryset(self):
        queryset = Debt.objects.filter(user=self.request.user).order_by('-created')

        debtor_id = self.request.query_params.get('debtorId', None)
        if debtor_id:
            queryset = queryset.filter(debtor_id=debtor_id)

        return queryset

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


class DebtorsViewSet(viewsets.ModelViewSet):
    serializer_class = DebtorSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        return Debtor.objects.filter(created_by=self.request.user).order_by('name')

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
