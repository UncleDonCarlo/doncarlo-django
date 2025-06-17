from apps.domain.task.models import TaskModel

class TaskRepository:
    def create(self, project_entity):
        return TaskModel.objects.create(
            title = project_entity.title,
            description = project_entity.description,
            startDate = project_entity.startDate,
            endDate = project_entity.endDate
        )
    
    def get_all_task(self):
        return TaskModel.objects.raw('SELECT * FROM task_taskmodel')