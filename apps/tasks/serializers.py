from rest_framework import serializers

from apps.tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'status', 'user', 'created_at', 'updated_at']
        extra_kwargs = {
            'id': {'read_only': True},
            'title': {'required': True},
            'status': {'required': True},
            'user': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True}
        }
