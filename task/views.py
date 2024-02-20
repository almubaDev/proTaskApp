from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .forms.forms import CreateTaskForm
from .models import Task


def landing(request):
    return render(request, 'task/index.html', {})


@login_required
def tasks_home(request):
    mostar_menu = True
    tasks_all = Task.objects.filter(task_owner=request.user)
    return render(request, 'task/tasks_home.html', {
             'create_task_form': CreateTaskForm(user=request.user),
             'tasks_all': tasks_all,
             'mostrar_menu' : mostar_menu
         })
    
    
@login_required
def perfil(request):
    return render(request, 'task\perfil.html',{})


@login_required
def create_task(request, id=None):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task =  form.save(commit=False)
            task.task_owner_id = id
            task.save()
            return redirect('tasks_home')


@login_required
def edit_task(request,id=None):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        edit_task = CreateTaskForm(request.POST, instance=task)
        if edit_task.is_valid():
            edit_task.save()
            return redirect('tasks_home')
    
    form_edit_task = CreateTaskForm(instance=task)
    return render(request,'task/edit_task.html', {
        'edit_task_form' : form_edit_task,
        'task_id' : id
     })
    
@login_required
def delete_task(request, id=None):
    delete_task = get_object_or_404(Task, id=id)
    delete_task.delete()
    return redirect('tasks_home')