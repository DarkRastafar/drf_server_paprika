from django.contrib import admin

from notes.functions.admin_functions import return_notebook_link
from notes.models import Note, Notebook


main_list_display = ['label', 'user']


@admin.register(Notebook)
class NotebookAdmin(admin.ModelAdmin):
    list_display = main_list_display.copy()


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = main_list_display.copy()
    list_display.insert(1, 'notebook_link')

    @admin.display(description='Блокнот')
    def notebook_link(self, obj):
        return return_notebook_link(obj)
