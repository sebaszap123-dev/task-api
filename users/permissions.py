from rest_framework.permissions import BasePermission
from rest_framework.throttling import AnonRateThrottle

class CustomAuthUser(BasePermission):
    """
    Permite el acceso no autenticado solo para el método POST (crear).
    """
    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return request.user and request.user.is_authenticated


class UserAnonRateThrottle(AnonRateThrottle):
    """
    Throttle personalizada que se aplica solo a métodos POST para usuarios anónimos.
    """
    def allow_request(self, request, view):
        if request.method == 'POST':
            return super().allow_request(request, view)
        return True
