from django.db import models

# Create your models here.
class Todo(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Urgent', '🔥 Blaze Mode'),  # Funny term for highest priority
    ]

    title = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField('Created', auto_now_add=True)
    updated_at = models.DateTimeField('UpdatedAt', auto_now=True)
    isCompleted = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='low')

    def __str__(self):
        return self.title
