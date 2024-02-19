from django.db import models
from user_manager.models import CustomUser

class Tag(models.Model):
    tag_name = models.CharField(max_length=10, verbose_name='Etiqueta')
    owner_tag = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.tag_name
    
    
class Priority(models.Model):
    priority_level =  models.CharField(max_length=10, verbose_name='Prioridad')
    owner_priority = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Priorities'
    
    def __str__(self):
        return self.priority_level
    
    
class Task(models.Model):
    STATUS_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('En progreso', 'En progreso'),
        ('Completada', 'Completada'),
    ]

    title = models.CharField(max_length=50, blank=False,  
                             null=False)
    
    description = models.TextField(blank=True, null=True)
    
    deadline = models.DateField()
    
    status = models.CharField(max_length=11, choices=STATUS_CHOICES,
                              default='Pendiente')
    
    task_owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    
    task_tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    
    task_priority = models.ForeignKey(Priority, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.title} > {self.task_owner}'
