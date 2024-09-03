from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Note
from .serializers import NotesSerializer



# Create your views here.

class NotesViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None
    serializer_class = NotesSerializer

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user).order_by('-created')

