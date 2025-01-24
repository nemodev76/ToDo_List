from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def add_task(request):
    task = request.POST['task']
    Task.objects.create(title=task)
    return redirect('home')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return render(request, 'home.html')

def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_completed = not task.is_completed
    task.save()
    return render(request, 'home.html')

# def task_detail(request, task_id):
#     task = Task.objects.get(id=task_id)
#     return render(request, 'tasks/task_detail.html', {'task': task})