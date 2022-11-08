from django.contrib import admin

from notes.functions.admin_functions import return_notebook_link
from notes.models import Note, Notebook, Record


main_list_display = ['label', 'user']


@admin.register(Notebook)
class NotebookAdmin(admin.ModelAdmin):
    list_display = main_list_display.copy()


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = main_list_display.copy()
    list_display.insert(1, 'body')
    list_display.insert(2, 'notebook_link')

    @admin.display(description='Блокнот')
    def notebook_link(self, obj):
        return return_notebook_link(obj)


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['note', 'record', 'date_create', 'get_user']

    @admin.display(description='Пользователь')
    def get_user(self, obj):
        if current_note := obj.note:
            return current_note.user
