from django.contrib.auth import get_user_model


class UserService:
    @staticmethod
    def register_user(validated_data):
        user = get_user_model().objects.create_user(
            phone_number=validated_data['phone_number'],
            password=validated_data['password'],
        )
        return user
