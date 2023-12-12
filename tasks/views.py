from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.core.paginator import Paginator


def task_list(request):
    tasks = Task.objects.all()

    paginator = Paginator(tasks, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'page_obj': page_obj
    })

def task_detail(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task_detail.html', {
        'task': task
    })

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')

    else:
        form = TaskForm()
    return render(request, 'tasks/task_create.html', {
        'form': form
    })

def task_edit(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_create.html', {
        'form': form
    })


def task_delete(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return redirect('task_list')