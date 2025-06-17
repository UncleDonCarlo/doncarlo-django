from rest_framework import serializers
from apps.domain.task.models import TaskModel

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ['title', 'description', 'startDate', 'endDate']
