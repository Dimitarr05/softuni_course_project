from django.shortcuts import render, redirect, get_object_or_404

from .forms import TaskForm
from .models import Task

# Create your views here.

def task_list(request):
    tasks = Task.objects.all()

    context = {
        "tasks": tasks,
    }

    return render(request, "tasks/task_list.html", context)

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("tasks:task_list")
    else:
        form = TaskForm()

    context = {
        "form": form,
    }

    return render(request, "tasks/task_form.html", context)


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect("tasks:task_list")
    else:
        form = TaskForm(instance=task)

    context = {
        "form": form,
        "task": task,
    }

    return render(request, "tasks/task_form.html", context)

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        task.delete()
        return redirect("tasks:task_list")

    return render(request,"tasks/task_confirm_delete.html",{"task": task})