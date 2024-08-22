from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.

class Debtor(models.Model):
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Debtor'
        verbose_name_plural = 'Debtors'


class Debt(TimeStampedModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE, blank=False, null=False, default=1)

    def __str__(self):
        return f"{self.description} - {self.amount}"

    class Meta:
        verbose_name = 'Debt'
        verbose_name_plural = 'Debts'
