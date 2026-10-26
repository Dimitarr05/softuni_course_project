from django import forms
from .models import Task, Category


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

    def clean_title(self):
        title = self.cleaned_data["title"].strip()

        if len(title) < 3:
            raise forms.ValidationError("The task title must contain at least 3 characters.")

        return title

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]

        labels = {
            "name": "Category name",
            "description": "Description",
        }

        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "e.g. University"}
            ),
            "description": forms.Textarea(
                attrs={"rows": 3}
            ),
        }

    def clean_name(self):
        name = self.cleaned_data["name"].strip()

        if len(name) < 2:
            raise forms.ValidationError(
                "The category name must contain at least 2 characters."
            )

        return name