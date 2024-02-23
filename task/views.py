from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .forms.forms import CreateTaskForm, CreateTagForm, CreatePriorityForm
from .models import Task, Tag, Priority


def landing(request):
    return render(request, 'task/index.html', {})

# Task Views
@login_required
def tasks_home(request):
    mostar_menu = True
    
    count_pending_tasks = Task.objects.filter(status='Pendiente', task_owner=request.user).count()
    count_tasks_in_process = Task.objects.filter(status='En progreso', task_owner=request.user).count()
    count_completed_tasks = Task.objects.filter(status='Completada', task_owner=request.user).count()
    count_expired_tasks = Task.objects.filter(status='Expirada', task_owner=request.user).count()
    count_tasks_all = Task.objects.filter(task_owner=request.user).count()
    tasks_all = Task.objects.filter(task_owner=request.user).order_by('deadline')
    
    CreateTaskForm.Meta.exclude = ('status',)
    return render(request, 'task/tasks_home.html', {
             'create_task_form': CreateTaskForm(user=request.user),
             'tasks_all': tasks_all,
             'mostrar_menu' : mostar_menu,
             'count_tasks_all': count_tasks_all,
             'count_pending_tasks' : count_pending_tasks,
             'count_tasks_in_process' : count_tasks_in_process,
             'count_completed_tasks' : count_completed_tasks,
             'count_expired_tasks' : count_expired_tasks
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
        edit_task = CreateTaskForm(request.POST,  instance=task)
        if edit_task.is_valid():
            edit_task.save()
            return redirect('tasks_home')

    form_edit_task = CreateTaskForm(user=request.user, instance=task)
    return render(request,'task/edit_task.html', {
        'edit_task_form' : form_edit_task,
        'task_id' : id
     })
    
    
@login_required
def delete_task(request, id=None):
    delete_task = get_object_or_404(Task, id=id)
    delete_task.delete()
    return redirect('tasks_home')


#Tags Views
@login_required
def tags_manager(request):
    tags = Tag.objects.filter(owner_tag=request.user.id)
    return render(request, 'task/tags_manager.html', {
        'tags': tags,
        'create_tag_form': CreateTagForm()
    })


@login_required
def create_tag(request, id):
    if request.method == 'POST':
        form = CreateTagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.owner_tag_id = id
            tag.save()
            
            return redirect('tags_manager')
        else:
            return HttpResponse('wey')


@login_required
def delete_tag(request, id):
    delete_tag = get_object_or_404(Tag, id=id)
    delete_tag.delete()
    return redirect('tags_manager')


@login_required
def priorities_manager(request):
    priorities = Priority.objects.filter(owner_priority=request.user.id)
    return render(request, 'task/priorities_manager.html',{
        'priorities': priorities,
        'create_priority_form': CreatePriorityForm()
    })
    

@login_required
def create_priority(request, id):
    if request.method == 'POST':
        form = CreatePriorityForm(request.POST)
        if form.is_valid():
            priority = form.save(commit=False)
            priority.owner_priority_id = id
            priority.save()
            return redirect('priorities_manager')
            
    
    
      
@login_required
def delete_priority(request, id):
    delete_priority = get_object_or_404(Priority,id=id)
    delete_priority.delete()
    return redirect('priorities_manager')