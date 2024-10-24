from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.tasks import views

app_name = 'tasks'

router = DefaultRouter()
router.register('', views.TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
]
