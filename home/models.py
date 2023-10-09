from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    taskTitle = models.CharField(max_length=30)
    taskDesc = models.TextField()
    time = models.DateTimeField()
    complete=models.BooleanField(default=False)
    


    def __str__ (self):
        return self.taskTitle

