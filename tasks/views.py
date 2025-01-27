from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def add_task(request):
    title = request.POST['task_title']
    Task.objects.create(title=title)
    return redirect('home')

def check_task(request, id):
    task = Task.objects.get(id=id)
    task.is_completed = True
    task.save()
    return redirect('home')

def uncheck_task(request, id):
    task = Task.objects.get(id=id)
    task.is_completed = False
    task.save()
    return redirect('home')

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('home')

def edit_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        new_title = request.POST.get('new_task_title')
        task.title = new_title
        task.save()
        return redirect('home')
        # return JsonResponse({'success': True, 'new_task': new_task})
    # return JsonResponse({'success': False, 'error': 'Invalid request'})
    return render(request, 'tasks/edit_task.html', {'task': task})

# def task_detail(request, id):
#     task = Task.objects.get(id=id)
#     return render(request, 'tasks/task_detail.html', {'task': task})