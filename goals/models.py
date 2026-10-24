from django.db import models

# Create your models here.

class Goal(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    deadline = models.DateField(null=True, blank=True)

    is_completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    tasks = models.ManyToManyField(
        "tasks.Task",
        blank=True,
        related_name="goals",
    )

    def __str__(self):
        return self.title
