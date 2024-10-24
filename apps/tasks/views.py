from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.tasks.filters import TaskFilter
from apps.tasks.models import Task
from apps.tasks.serializers import TaskSerializer
from apps.tasks.services import TaskService
from apps.utils.cutom_permissions import IsRegularUser


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_class = TaskFilter

    permission_classes = [IsRegularUser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        TaskService.create_task(request, serializer.validated_data)

        response_data = {
            'data': serializer.data,
            'message': 'Task created successfully'
        }
        return Response(response_data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        if self.request.user.user_type == 'regular':
            return self.queryset.filter(user=self.request.user)
        return self.queryset
