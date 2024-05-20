from django.urls import path
from .views import hello_world

urlpatterns = [
    path('tasks/', hello_world, name='hello-world'),
]