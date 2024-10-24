from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from apps.tasks.models import Task


class TaskViewSetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('tasks:tasks-list')

        self.regular_user_1 = get_user_model().objects.create_user(
            phone_number='989351234567', password='123'
        )
        self.regular_user_2 = get_user_model().objects.create_user(
            phone_number='989351234486', password='123'
        )
        self.admin_user = get_user_model().objects.create(
            phone_number='989359876543', password=make_password('123'), user_type='admin'
        )

        self.regular_user_1_token = RefreshToken.for_user(self.regular_user_1).access_token
        self.regular_user_2_token = RefreshToken.for_user(self.regular_user_2).access_token
        self.admin_user_token = RefreshToken.for_user(self.admin_user).access_token

        self.task1 = Task.objects.create(title="Task 1", status="in_progress", user=self.regular_user_1)
        self.task2 = Task.objects.create(title="Task 2", status="completed", user=self.regular_user_1)
        self.task3 = Task.objects.create(title="Task 2", status="completed", user=self.regular_user_2)

    def authenticate_user(self, user_token):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {user_token}')

    def test_unauthenticated_user(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_regular_user_list_own_tasks(self):
        self.authenticate_user(self.regular_user_1_token)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        for task in response.data:
            self.assertEqual(task['user'], self.regular_user_1.id)

    def test_regular_user_create_new_task(self):
        self.authenticate_user(self.regular_user_1_token)

        data = {
            "title": "new task",
            "status": "in_progress"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.filter(user_id=self.regular_user_1.id).count(), 3)

    def test_regular_user_can_update_task_method_patch(self):
        self.authenticate_user(self.regular_user_1_token)

        data = {
            "title": "updated task"
        }

        url = f'{self.url}{str(self.task1.id)}/'
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.get(id=self.task1.id).title, "updated task")

    def test_regular_user_can_delete_own_task(self):
        self.authenticate_user(self.regular_user_1_token)

        url = f'{self.url}{str(self.task1.id)}/'
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.filter(user_id=self.regular_user_1.id).count(), 1)

    def test_regular_user_2_cannot_access_regular_user_one_tasks(self):
        self.authenticate_user(self.regular_user_2_token)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.filter(user_id=self.regular_user_2.id).count(), 1)

    def test_admin_user_cannot_access_tasks(self):
        self.authenticate_user(self.admin_user_token)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
