from rest_framework import serializers


class BaseNoteSerializer(serializers.Serializer):
    label = serializers.CharField(default='Без названия')
    user = serializers.IntegerField()


class NotebookSerializer(BaseNoteSerializer):
    ...


class NoteSerializer(BaseNoteSerializer):
    notebook = serializers.IntegerField(default=None)
