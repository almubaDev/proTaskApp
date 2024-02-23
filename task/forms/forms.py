from django.forms import ModelForm
from django import forms
from django.utils import timezone
from user_manager.models import CustomUser
from ..models import Task, Tag, Priority

#Task forms

class CreateTaskForm(ModelForm): 
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CreateTaskForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['task_tag'].queryset = Tag.objects.filter(owner_tag=user)
            self.fields['task_priority'].queryset = Priority.objects.filter(owner_priority=user)

    class Meta:
        model = Task
        exclude = ('task_owner',)
        labels = {'title' : 'Título',
                  'description' : 'Detalles',
                  'deadline' : 'Fecha límite',
                  'status' : 'Estado',
                  'task_tag' : 'Etiqueta',
                  'task_priority' : 'Prioridad'  
                }
        widgets = {
            'deadline' : forms.DateInput(attrs={'type':'date', 'id':'fecha', 'value': {timezone.now().date()}})

        }
 
    
class CreateTagForm(ModelForm):
    class Meta:
        model = Tag
        exclude = ('owner_tag',)
        labels = {'tag_name' : 'Nombre de la etiqueta'} 


class CreatePriorityForm(ModelForm):
    class Meta:
        model = Priority
        exclude = ('owner_priority',)
        labels = {'priority_level': 'Nivel de Prioridad'}