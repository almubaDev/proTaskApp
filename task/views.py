from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .forms.forms import CreateTaskForm


def landing(request):
    return render(request, 'task/index.html', {})

@login_required
def tasks_home(request):
    return render(request, 'task/tasks_home.html', {
             'create_task_form': CreateTaskForm(user=request.user),
         })


@login_required
def perfil(request):
    return render(request, 'task\perfil.html',{})

@login_required
def create_task(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST, user=request.user)
        if form.is_valid():
            task =  form.save(commit=False)
            task.task_owner_id = request.user
            task.save()
            return redirect('tasks_home')

    