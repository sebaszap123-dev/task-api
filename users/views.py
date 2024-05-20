from rest_framework import viewsets

from users.models import NiceUser
from users.permissions import CustomAuthUser, UserAnonRateThrottle
from users.serializers import NiceUserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.throttling import AnonRateThrottle

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = NiceUserSerializer
    permission_classes = (CustomAuthUser,)
    # Throttle class for prevent DDoS Attacks
    throttle_classes = [UserAnonRateThrottle]
    queryset = NiceUser.objects.all()


class CustomAuthToken(ObtainAuthToken):
    permission_classes = (AllowAny,)
    throttle_classes = [AnonRateThrottle]
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })