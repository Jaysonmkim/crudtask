from django.db import models

class Task(models.Model):
    Title = models.CharField(max_length=20)
    Description = models.TextField()
    completed = models.BooleanField(default=False)
    Created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Title
# Create your models here.
