from django.contrib.auth.models import User
from rest_framework import serializers
from notes.models import Note, Notebook


class BaseNoteSerializer(serializers.Serializer):
    label = serializers.CharField(default='Без названия')
    user = serializers.CharField()


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)


class NotebookSerializer(BaseNoteSerializer):
    ...


class NoteSerializer(serializers.ModelSerializer):
    # body = serializers.CharField(default='')
    # notebook = serializers.CharField(required=False, default=None)
    # user = UserSerializer()

    # def validate_notebook(self, value):
    #     notebook_qw = Notebook.objects.filter(label=value)
    #     if not notebook_qw.exists():
    #         raise serializers.ValidationError(f'Блокнот <{value}> - не существует')
    #     else:
    #         return notebook_qw.first()
    #
    # def validate_user(self, value):
    #     user_qw = User.objects.filter(username=value)
    #     if not user_qw.exists():
    #         raise serializers.ValidationError(f'Unknown error')
    #     else:
    #         return user_qw.first()

    # def create(self, validated_data):
    #     return Note.objects.create(**validated_data)

    class Meta:
        model = Note
        fields = ('label', 'body', 'notebook', 'user')
