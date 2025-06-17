from apps.domain.task.models import TaskModel

class TaskRepository:
    def create(self, task_entity):
        return TaskModel.objects.create(
            title = task_entity.title,
            description = task_entity.description,
            startDate = task_entity.startDate,
            endDate = task_entity.endDate,
            project = task_entity.project,
        )
    
    def get_all_task(self):
        return TaskModel.objects.select_related('project').all()