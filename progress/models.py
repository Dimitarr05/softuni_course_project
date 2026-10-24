from django.db import models

# Create your models here.

class TaskActivity(models.Model):
    ACTION_CHOICES = [
        ("created", "Created"),
        ("updated", "Updated"),
        ("completed", "Completed"),
    ]

    task = models.ForeignKey(
        "tasks.Task",
        on_delete=models.CASCADE,
        related_name="activities",
    )

    action = models.CharField(
        max_length=20,
        choices=ACTION_CHOICES,
    )

    description = models.CharField(
        max_length=255,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task.title} - {self.action}"
