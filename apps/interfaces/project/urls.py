from django.urls import path
from apps.interfaces.project.Projectviews import ProjectUserView

urlpatterns = [
    path('', ProjectUserView.as_view(), name='project'),
]
