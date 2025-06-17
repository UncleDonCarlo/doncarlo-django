from django.db import models

class ProjectModel(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'project'