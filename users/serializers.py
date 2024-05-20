from rest_framework import serializers

from users.models import NiceUser

class NiceUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = NiceUser
        fields = ('id', 'email',)