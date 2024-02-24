from django.utils import timezone
from .models import Task
import requests

def mark_expired_tasks():
    # Obtener todas las tareas pendientes y en progreso cuya fecha límite ha pasado
    expired_tasks = Task.objects.filter(status__in=['Pendiente', 'En progreso'], deadline__lt=timezone.now())
    
    # Cambiar el estado de las tareas expiradas a "Expirada"
    expired_tasks.update(status='Expirada')

def weather(city):
    url ='https://api.openweathermap.org/data/2.5/weather?q={}&appid=6872202ba2faccc0869231bbc93d0207&units=metric'.format(city)

    res = requests.get(url)
    data = res.json()
    
    return data