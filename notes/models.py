from django.contrib.auth.models import User
from django.db import models


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
    notebook = models.ForeignKey(Notebook, verbose_name='Блокнот', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.label}'

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
