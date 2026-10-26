from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm, CategoryForm
from .models import Task,Category
from progress.models import TaskActivity

# Create your views here.


def task_list(request):
    tasks = Task.objects.all()

    status = request.GET.get("status")
    priority = request.GET.get("priority")

    if status:
        tasks = tasks.filter(status=status)

    if priority:
        tasks = tasks.filter(priority=priority)

    tasks = tasks.order_by("due_date")

    return render(
        request,
        "tasks/task_list.html",
        {"tasks": tasks}
    )


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save()

            TaskActivity.objects.create(
                task=task,
                action="created",
                description="Task was created."
            )

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
            task = form.save()

            TaskActivity.objects.create(
                task=task,
                action="updated",
                description="Task was updated."
            )

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

def category_list(request):
    categories = Category.objects.all()

    return render(
        request,
        "tasks/category_list.html",
        {"categories": categories}
    )


def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("tasks:category_list")
    else:
        form = CategoryForm()

    return render(
        request,
        "tasks/category_form.html",
        {"form": form}
    )


def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    task.status = "completed"
    task.save()

    TaskActivity.objects.create(
        task=task,
        action="completed",
        description="Task was completed."
    )

    return redirect("tasks:task_list")


def task_list(request):
    tasks = Task.objects.all()

    status = request.GET.get("status")
    priority = request.GET.get("priority")

    if status:
        tasks = tasks.filter(status=status)

    if priority:
        tasks = tasks.filter(priority=priority)

    tasks = tasks.order_by("due_date")

    return render(
        request,
        "tasks/task_list.html",
        {"tasks": tasks}
    )
