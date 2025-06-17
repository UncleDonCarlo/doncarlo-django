from django.urls import path
from apps.interfaces.task.Taskviews import TaskView

urlpatterns = [
    path('', TaskView.as_view(), name='task'),
]
