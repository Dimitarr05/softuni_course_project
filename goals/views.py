from django.shortcuts import render, redirect, get_object_or_404
from .forms import GoalForm
from .models import Goal
# Create your views here.

def goal_list(request):
    goals = Goal.objects.all().order_by("-created_at")

    return render(
        request,
        "goals/goal_list.html",
        {"goals": goals},
    )

def goal_create(request):
    if request.method == "POST":
        form = GoalForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("goals:goal_list")
    else:
        form = GoalForm()

    return render(
        request,
        "goals/goal_form.html",
        {"form": form},
    )

def goal_detail(request, pk):
    goal = get_object_or_404(Goal, pk=pk)

    return render(
        request,
        "goals/goal_detail.html",
        {"goal": goal},
    )

def goal_update(request, pk):
    goal = get_object_or_404(Goal, pk=pk)

    if request.method == "POST":
        form = GoalForm(request.POST, instance=goal)

        if form.is_valid():
            form.save()
            return redirect("goals:goal_detail", pk=goal.pk)
    else:
        form = GoalForm(instance=goal)

    return render(
        request,
        "goals/goal_form.html",
        {"form": form, "goal": goal},
    )

def goal_delete(request, pk):
    goal = get_object_or_404(Goal, pk=pk)

    if request.method == "POST":
        goal.delete()
        return redirect("goals:goal_list")

    return render(
        request,
        "goals/goal_confirm_delete.html",
        {"goal": goal},
    )