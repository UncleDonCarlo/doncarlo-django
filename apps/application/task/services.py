from apps.domain.task.models import TaskModel
from apps.infrastructure.task.repositories import TaskRepository
from apps.domain.project.models import ProjectModel
from django.core.exceptions import ObjectDoesNotExist

class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def add_task(self, title, description,start_date, end_date, project):
        try:
            project_instance = ProjectModel.objects.get(id=project)
        except ObjectDoesNotExist:
            return {
                "error" : f"Project with id {project} not found"
            }

        project = TaskModel(
            title = title,
            description = description,
            startDate = start_date,
            endDate = end_date,
            project = project_instance
        )
        return self.repository.create(project)

    def get_all_task(self):
        return self.repository.get_all_task()