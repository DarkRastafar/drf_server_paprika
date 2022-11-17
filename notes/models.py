from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models

from notes.functions.models_functions import get_path_upload_record, user_directory_path
from notes.validators import validate_size_image
from project.settings import ALLOWED_IMAGE_EXTENSIONS


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
    note = models.ForeignKey(
        Note,
        verbose_name='Заметка',
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    record = models.FileField(
        'Запись',
        upload_to=get_path_upload_record,
        validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav'])]
    )
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True, blank=True)
    date_create = models.DateTimeField(verbose_name='Дата загрузки', auto_now_add=True)

    def __str__(self):
        return f'{self.record}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class HairPhotos(ABSLabel):
    photo = models.ImageField(
        upload_to=user_directory_path,
        validators=[
            FileExtensionValidator(allowed_extensions=ALLOWED_IMAGE_EXTENSIONS),
            validate_size_image
        ]
    )

    def __str__(self):
        return f'{self.label}, {self.photo}'

    class Meta:
        verbose_name = 'Фото прически'
        verbose_name_plural = 'Фото причесок'


class CategoryMove(models.Model):
    category = models.CharField(max_length=120, verbose_name='Категория', db_index=True)

    def __str__(self):
        return f'{self.category}'

    class Meta:
        verbose_name = 'Категория фильма'
        verbose_name_plural = 'Категории фильмов'


class MoveBeLike(ABSLabel):
    category = models.ManyToManyField(CategoryMove, verbose_name='Категория', blank=True)

    def __str__(self):
        return f'{self.label}'

    class Meta:
        verbose_name = 'Фото прически'
        verbose_name_plural = 'Фото причесок'
