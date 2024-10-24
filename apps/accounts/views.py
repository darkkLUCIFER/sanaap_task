from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from apps.accounts.serializers import UserRegisterSerializer, UserLoginSerializer
from apps.accounts.services import UserService


class UserRegisterView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=UserRegisterSerializer,
        responses={
            201: openapi.Response('User registered successfully', UserRegisterSerializer),
            400: openapi.Response('Bad Request', openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                'detail': openapi.Schema(type=openapi.TYPE_OBJECT, description='Invalid phone number.')
            })),
        }
    )
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = UserService.register_user(serializer.validated_data)

        refresh = RefreshToken.for_user(user)
        response_data = {
            "user": serializer.data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        return Response(response_data, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=UserLoginSerializer,
        responses={
            200: openapi.Response('Login successful', UserLoginSerializer),
            400: openapi.Response('Bad Request', openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                'detail': openapi.Schema(type=openapi.TYPE_STRING, description='Invalid credentials')
            })),
        }
    )
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = UserService.login_user(request, serializer.validated_data)
        if user:
            refresh = RefreshToken.for_user(user)
            response_data = {
                "user": serializer.data,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
