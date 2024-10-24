from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['phone_number', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'phone_number': {'required': True},
        }


class UserLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True, max_length=12)
    password = serializers.CharField(required=True, write_only=True)
