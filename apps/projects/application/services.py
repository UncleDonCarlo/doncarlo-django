from projects.domain.models import ProjectModel
from projects.infrastructure.repositories import ProjectRepository

class ProjectService:
    def __init__(self, repository: ProjectRepository):
        self.repository = repository

    def add_project(self, title, description):
        project = ProjectModel(title=title, description=description)
        return self.repository.create(project)
