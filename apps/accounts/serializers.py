from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.accounts.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['phone_number']
        required_fields = ['phone_number']

    def validate_phone_number(self, value):
        user = User.objects.filter(phone_number=value)
        if user.exists():
            raise serializers.ValidationError('user already exists')
        return value
