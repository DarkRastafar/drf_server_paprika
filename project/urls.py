from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from notes.views import NoteViewSet, NotebookViewSet, RecordViewSet
from project.yasg import urlpatterns as yasg_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
]


router = DefaultRouter()
router.register(r'api/notes/note', NoteViewSet)
router.register(r'api/notes/notebook', NotebookViewSet)
router.register(r'api/notes/record', RecordViewSet)


urlpatterns += [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token)
]

urlpatterns += yasg_urlpatterns
