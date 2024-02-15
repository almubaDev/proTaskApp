from django.shortcuts import render

def tasks_home(request):
    return render(request, 'task/tasks_home.html', {})