

from django.utils import timezone
from .models import Task

def mark_expired_tasks():
    # Obtener todas las tareas pendientes y en progreso cuya fecha límite ha pasado
    expired_tasks = Task.objects.filter(status__in=['Pendiente', 'En progreso'], deadline__lt=timezone.now())
    
    # Cambiar el estado de las tareas expiradas a "Expirada"
    expired_tasks.update(status='Expirada')
