from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class UserRegisterTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('accounts:user-register')

    def test_register_user_with_valid_info(self):
        data = {
            'phone_number': '989876543212',
            'password': '123',
        }
        response = self.client.post(self.register_url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)
        self.assertIn('user', response.data)

    def test_register_duplicate_user(self):
        get_user_model().objects.create_user(phone_number='989876543212', password='123')

        data = {
            'phone_number': '989876543212',
            'password': '1237856',
        }

        response = self.client.post(self.register_url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('phone_number', response.data)

    def test_register_with_invalid_phone_number(self):
        data = {
            'phone_number': '09351234567',
            'password': '123',
        }

        response = self.client.post(self.register_url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('phone_number', response.data)


class UserLoginTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.login_url = reverse('accounts:user-login')
        self.user = get_user_model().objects.create_user(phone_number='989351234567', password='123')

    def test_login_user_with_valid_info(self):
        data = {
            'phone_number': '989351234567',
            'password': '123'
        }

        response = self.client.post(self.login_url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('user', response.data)
        self.assertIn('refresh', response.data)

    def test_login_user_not_registered(self):
        data = {
            'phone_number': '989359876543',
            'password': '123'
        }

        response = self.client.post(self.login_url, data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
