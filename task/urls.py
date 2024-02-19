from django.urls import path
from . import views
urlpatterns = [
    path("", views.landing, name="landing"),
    path("task/", views.tasks_home, name="tasks_home"),
    path("perfil/", views.perfil, name="perfil"),
    path("create/", views.create_task, name="create_task"),
]
