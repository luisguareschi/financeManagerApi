from rest_framework import permissions, viewsets
from .models import Note
from .serializers import NotesSerializer, CreateNoteSerializer


# Create your views here.

class NotesViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateNoteSerializer
        if self.action == 'update':
            return CreateNoteSerializer
        return NotesSerializer

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user).order_by('created')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
