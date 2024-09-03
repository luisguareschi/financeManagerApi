from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.

class Note(TimeStampedModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
