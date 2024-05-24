from django.urls import include, path
from rest_framework import routers
from .views import CustomAuthToken, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename="user")

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', CustomAuthToken.as_view())
]