from django.shortcuts import render, redirect

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