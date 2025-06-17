from rest_framework import serializers
from projects.domain.models import ProjectModel

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields = ['title', 'description']
