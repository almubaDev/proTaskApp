from django.urls import path
from . import views
urlpatterns = [
    path("", views.tasks_home, name="task_home")
]
