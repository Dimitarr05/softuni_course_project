from django import forms
from .models import TaskActivity

class ActivityForm(forms.ModelForm):
    class Meta:
        model = TaskActivity
        fields = ["task", "action", "description"]

        labels = {
            "task": "Task",
            "action": "Action",
            "description": "Description",
        }

        widgets = {
            "description": forms.TextInput(
                attrs={"placeholder": "Describe the activity..."}
            ),
        }

    def clean_description(self):
        description = self.cleaned_data["description"].strip()
        return description
