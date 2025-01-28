from django.shortcuts import render, redirect
from .models import Task
from django.contrib import messages

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        title = request.POST['task_title']
        Task.objects.create(title=title)
        return redirect('home')

def check_task(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.is_completed = True
        task.save()
        return redirect('home')

def uncheck_task(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.is_completed = False
        task.save()
        return redirect('home')

def delete_task(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        task.delete()
        return redirect('home')

def edit_task(request, id):
    if request.method == 'POST':
        task = Task.objects.get(id=id)
        new_title = request.POST.get('new_task_title')
        task.title = new_title
        task.save()
        return redirect('home')
    # return render(request, 'tasks/edit_task.html', {'task': task})
    
def clear_completed_tasks(request):
    if request.method == 'POST':
        Task.objects.filter(is_completed=True).delete()
        messages.success(request, "All completed tasks have been cleared!")
        return redirect('home')

# def task_detail(request, id):
#     task = Task.objects.get(id=id)
#     return render(request, 'tasks/task_detail.html', {'task': task})