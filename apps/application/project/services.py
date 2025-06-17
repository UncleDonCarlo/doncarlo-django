from apps.domain.project.models import ProjectModel
from apps.infrastructure.project.repositories import ProjectRepository

class ProjectService:
    def __init__(self, repository: ProjectRepository):
        self.repository = repository

    def add_project(self, title, description):
        project = ProjectModel(title=title, description=description)
        return self.repository.create(project)

    def get_all_project(self):
        return self.repository.get_all_project()
        