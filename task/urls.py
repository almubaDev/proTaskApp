from django.urls import path
from . import views
urlpatterns = [
    path("", views.landing, name="landing"),
    path("task/", views.tasks_home, name="tasks_home"),
    path("perfil/", views.perfil, name="perfil"),
    path("create/<int:id>", views.create_task, name="create_task"),
    path("edit/<int:id>", views.edit_task, name="edit_task"),
    path("delete/<int:id>", views.delete_task, name="delete_task"),
]