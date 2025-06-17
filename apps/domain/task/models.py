from django.db import models
from apps.domain.project.models import ProjectModel

class TaskModel(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'task'