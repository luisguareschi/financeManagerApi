from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.

class Note(TimeStampedModel):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return f"{self.title} - {self.user}" if self.title else f"Note - {self.user}"
