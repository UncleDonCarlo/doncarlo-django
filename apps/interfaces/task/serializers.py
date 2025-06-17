from rest_framework import serializers
from apps.domain.task.models import TaskModel
from apps.interfaces.project.serializers import ProjectSerializer

class TaskSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)
    
    class Meta:
        model = TaskModel
        fields = ['title', 'description', 'startDate', 'endDate', 'project']
