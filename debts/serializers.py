from rest_framework import serializers

from debts.models import Debt, Debtor


class DebtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debtor
        fields = [
            "id",
            "name",
            "created_by",
        ]


class DebtSerializer(serializers.ModelSerializer):
    debtor = DebtorSerializer()

    class Meta:
        model = Debt
        fields = [
            "id",
            "user",
            "description",
            "amount",
            "debtor",
            "created",
        ]
