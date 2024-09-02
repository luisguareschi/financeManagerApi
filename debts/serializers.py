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


class CreateDebtSerializer(serializers.ModelSerializer):
    debtor = serializers.CharField()
    created = serializers.DateTimeField(read_only=False)
    class Meta:
        model = Debt
        fields = [
            "description",
            "amount",
            "debtor",
            "created",
        ]

    def create(self, validated_data):
        debtor_id = validated_data.pop('debtor')
        # check if debtor id is a number
        debtor = None
        try:
            debtor_id = int(debtor_id)
            debtor = Debtor.objects.filter(id=debtor_id).first()
        except ValueError:
            pass
        if not debtor:
            debtor = Debtor.objects.create(name=debtor_id, created_by=validated_data['user'])

        debt = Debt.objects.create(debtor=debtor, **validated_data)
        return debt
