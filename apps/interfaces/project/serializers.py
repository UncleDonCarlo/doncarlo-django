from rest_framework import serializers
from apps.domain.project.models import ProjectModel

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = ['title', 'description']
