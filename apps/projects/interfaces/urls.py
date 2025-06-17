from django.urls import path
from apps.projects.interfaces.views import ProjectUserView

urlpatterns = [
    path('', ProjectUserView.as_view(), name='project'),
]
