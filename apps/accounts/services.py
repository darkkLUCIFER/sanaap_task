from django.contrib.auth import get_user_model, authenticate, login


class UserService:
    @staticmethod
    def register_user(validated_data):
        user = get_user_model().objects.create_user(
            phone_number=validated_data['phone_number'],
            password=validated_data['password'],
        )
        return user

    @staticmethod
    def login_user(request ,validated_data):
        user = authenticate(phone_number=validated_data['phone_number'], password=validated_data['password'])
        if user:
            login(request, user)
            return user
        else:
            return None
