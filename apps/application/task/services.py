from apps.domain.task.models import TaskModel
from apps.infrastructure.task.repositories import TaskRepository

class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def add_task(self, title, description,start_date, end_date):
        project = TaskModel(
            title = title,
            description = description,
            startDate = start_date,
            endDate = end_date
        )
        return self.repository.create(project)

    def get_all_task(self):
        return self.repository.get_all_task()