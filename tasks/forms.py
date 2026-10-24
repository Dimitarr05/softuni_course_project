
from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "category",
            "priority",
            "status",
            "due_date",
        ]

        labels = {
            "title": "Task title",
            "description": "Description",
            "category": "Category",
            "priority": "Priority",
            "status": "Status",
            "due_date": "Due date",
        }

        help_texts = {
            "title": "Enter a short and clear task title.",
            "due_date": "Choose the date by which the task should be completed.",
        }

        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "e.g. Study Django"}
            ),
            "description": forms.Textarea(
                attrs={"placeholder": "Describe your task...", "rows": 3}
            ),
            "due_date": forms.DateInput(
                attrs={"type": "date"}
            ),
        }
