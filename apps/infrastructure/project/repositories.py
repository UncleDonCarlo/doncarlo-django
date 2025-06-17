from apps.domain.project.models import ProjectModel

class ProjectRepository:
    def create(self, project_entity):
        return ProjectModel.objects.create(
            title=project_entity.title,
            description=project_entity.description,
        )
    
    def get_all_project(self):
        return ProjectModel.objects.raw('SELECT * FROM project_projectmodel')