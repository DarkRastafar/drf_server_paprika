from django.utils.html import format_html
from django.utils.safestring import mark_safe


def return_notebook_link(obj):
    if obj.notebook:
        url = f"/admin/notes/notebook/{obj.notebook.id}/change/"
        # js_string = f"windows.open('{url}', 'НазванияОкна', 'Toolbar=no, Location=no, ScrollBars=no, Width=500, Height=400')"
        link = mark_safe(
            f'<a href="{url}" target="_blank">{obj.notebook.label}</a>')
        # f'<a href="{url}" onClick="{js_string}">{obj.notebook.label}</a>'
        return format_html(f"{link}")
