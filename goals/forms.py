from django import forms
from .models import Goal

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = [
            "title",
            "description",
            "deadline",
            "is_completed",
            "tasks",
        ]

        labels = {
            "title": "Goal title",
            "description": "Description",
            "deadline": "Target date",
            "is_completed": "Completed",
            "tasks": "Related tasks",
        }

        help_texts = {
            "title": "Choose a clear title for your goal.",
            "tasks": "Select tasks that contribute to this goal.",
        }

        widgets = {
            "title": forms.TextInput(
                attrs={"placeholder": "e.g. Learn Django"}
            ),
            "description": forms.Textarea(
                attrs={
                    "placeholder": "Describe what you want to achieve...",
                    "rows": 3,
                }
            ),
            "deadline": forms.DateInput(
                attrs={"type": "date"}
            ),
        }

    def clean_title(self):
        title = self.cleaned_data["title"].strip()

        if len(title) < 3:
            raise forms.ValidationError("The goal title must contain at least 3 characters.")

        return title