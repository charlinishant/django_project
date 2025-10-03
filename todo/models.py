from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = (
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_CHOICES, default=2)

    class Meta:
        ordering = ['completed', 'priority', '-created_at']

    def __str__(self):
        return self.title
