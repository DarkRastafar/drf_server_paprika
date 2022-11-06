from django.db import models


class Note(models.Model):
    label = models.CharField(
        max_length=256, verbose_name='Название заметки', null=True, blank=True, default='Без названия'
    )

    def __str__(self):
        return f'{self.label}'

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
