from django.urls import path
from .views import TaskViewSet
from django.urls import include, path
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, basename="tasks")

urlpatterns = [
    path('', include(router.urls)),
]