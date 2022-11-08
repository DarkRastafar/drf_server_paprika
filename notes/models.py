from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models

from notes.functions.models_functions import get_path_upload_record


class ABSLabel(models.Model):
    label = models.CharField(
        max_length=256, verbose_name='Название', null=True, blank=True, default='Без названия'
    )
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        abstract = True


class Notebook(ABSLabel):

    def __str__(self):
        return f'{self.label}'

    class Meta:
        verbose_name = 'Блокнот'
        verbose_name_plural = 'Блокноты'


class Note(ABSLabel):
    body = models.TextField(verbose_name='Тело заметки', null=True, blank=True, default='')
    notebook = models.ForeignKey(Notebook, verbose_name='Блокнот', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.label}'

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'


class Record(models.Model):
    note = models.ForeignKey(Note, verbose_name='Заметка', on_delete=models.CASCADE, null=True, blank=True)
    record = models.FileField(
        'Запись',
        upload_to=get_path_upload_record,
        validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav'])]
    )
    date_create = models.DateTimeField(verbose_name='Дата загрузки', auto_now_add=True)

    def __str__(self):
        return f'{self.record}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
