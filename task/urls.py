from django.urls import path
from . import views
urlpatterns = [
    #Task
    path("", views.landing, name="landing"),
    path("task/", views.tasks_home, name="tasks_home"),
    path("perfil/", views.perfil, name="perfil"),
    path("create/<int:id>", views.create_task, name="create_task"),
    path("edit/<int:id>", views.edit_task, name="edit_task"),
    path("delete/<int:id>", views.delete_task, name="delete_task"),
    # Tags
    path("tags/", views.tags_manager, name="tags_manager"),
    path("tags/create/<int:id>", views.create_tag, name="create_tag"),
    path("tags/delete/<int:id>", views.delete_tag, name="delete_tag"),
    
    # Prioriies
    path("priorities/", views.priorities_manager, name="priorities_manager"),
    path("priorities/create/<int:id>", views.create_priority, name="create_priority"),
    path("priorities/delete/<int:id>", views.delete_priority, name="delete_priority"),
]