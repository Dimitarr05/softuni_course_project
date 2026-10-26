from django.shortcuts import render, redirect
from .models import TaskActivity
from .forms import ActivityForm

# Create your views here.


def progress_list(request):
    activities = TaskActivity.objects.all().order_by("-created_at")

    return render(request,"progress/progress_list.html",{"activities": activities}
    )


def activity_create(request):
    if request.method == "POST":
        form = ActivityForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("progress:progress_list")
    else:
        form = ActivityForm()

    return render(
        request,
        "progress/activity_form.html",
        {"form": form}
    )
