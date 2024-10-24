from django.db import models
from apps.utils.base_model import BaseModel


class Task(BaseModel):
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'

    STATUS_CHOICES = [
        (IN_PROGRESS, 'In progress'),
        (COMPLETED, 'Completed'),
    ]

    title = models.CharField(max_length=100, verbose_name='Title')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=IN_PROGRESS)
