from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from notes.models import Note, Notebook, Record
from notes.serializers import NoteSerializer, NotebookSerializer, RecordSerializer


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class NotebookViewSet(ModelViewSet):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class RecordViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
