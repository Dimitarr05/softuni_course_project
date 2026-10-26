from django.urls import path
from . import views

app_name = "progress"

urlpatterns = [
    path("", views.progress_list, name="progress_list"),
    path("create/", views.activity_create, name="activity_create"),
]
