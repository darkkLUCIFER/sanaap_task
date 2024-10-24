from django.urls import path
from apps.accounts import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user-register'),
    path('login/', views.UserLoginView.as_view(), name='user-login'),
]
