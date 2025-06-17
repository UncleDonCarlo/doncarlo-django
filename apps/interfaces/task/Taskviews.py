from apps.application.task.services import TaskService
from apps.infrastructure.task.repositories import TaskRepository
from .serializers import TaskSerializer
from apps.domain.project.models import ProjectModel
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Tasks'])
class TaskView(APIView):
    queryset = ProjectModel.objects.all()
    serializer_class = TaskSerializer

    def post(self, request):
        data = request.data
        title = data.get('title')
        description = data.get('description')
        start_date = data.get('startDate')
        end_date = data.get('endDate')
        project = data.get('project')

        if not title or not description:
            return Response(
                {
                    "error": "title and description are required"
                },
                status = 400
            )

        service = TaskService(TaskRepository())
        task = service.add_task(title, description, start_date, end_date, project)

        if isinstance(task, dict) and task.get("error"):
            return Response(task, status=400)
        
        return Response({
            "title": task.title,
            "description": task.description,
            "startDate": task.startDate,
            "endDate": task.endDate,
            "project": {
                "id": task.project.id,
                "title": task.project.title,
            }
        })
    
    def get(self, request):
        service = TaskService(TaskRepository())
        projects = service.get_all_task()
        serializer = self.serializer_class(projects, many=True)

        return Response({
            "data": serializer.data
        })
