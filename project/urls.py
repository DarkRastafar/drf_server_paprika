from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from notes.views import NoteViewSet, NotebookViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
]


router = DefaultRouter()
router.register(r'api/notes/note', NoteViewSet)
router.register(r'api/notes/notebook', NotebookViewSet)


urlpatterns += [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token)
]
