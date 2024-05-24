from rest_framework import serializers

from users.models import NiceUser
from django.contrib.auth.password_validation import validate_password

class NiceUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = NiceUser
        fields = ('id', 'email', 'password',)

    def validate_password(self, value):
        # Valida la contraseña usando los validadores de Django
        validate_password(value)
        return value

    def create(self, validated_data):
        user = NiceUser(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance