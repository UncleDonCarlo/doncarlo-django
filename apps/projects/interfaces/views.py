from projects.application.services import ProjectService
from projects.infrastructure.repositories import ProjectRepository
from .serializers import ProjectSerializer
from projects.domain.models import ProjectModel
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['Projects'])
class ProjectUserView(APIView):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectSerializer

    def post(self, request):
        data = request.data
        title = data.get('title')
        description = data.get('description')

        if not title or not description:
            return Response(
                {
                    "error": "title and description are required"
                },
                status = 400
            )

        service = ProjectService(ProjectRepository())
        project = service.add_project(title, description)
        
        return Response(
            {
                "id": project.id,
                "title": project.title,
                "description": project.description
            }
        )
