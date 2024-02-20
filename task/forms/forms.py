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
        exclude = ('status', 'task_owner')
        labels = {'title' : 'Título',
                  'description' : 'Detalles',
                  'deadline' : 'Fecha límite',
                  'task_tag' : 'Etiqueta',
                  'task_priority' : 'Prioridad'  
                }
        widgets = {
            'deadline' : forms.DateInput(attrs={'type':'date', 'value': {timezone.now().date()}})

        }