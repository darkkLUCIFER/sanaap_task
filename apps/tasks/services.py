from apps.tasks.models import Task


class TaskService:
    @staticmethod
    def create_task(request, validated_data):
        Task.objects.create(
            title=validated_data['title'],
            status=validated_data['status'],
            user_id=request.user.id
        )
