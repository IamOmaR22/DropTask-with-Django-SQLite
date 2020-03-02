from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TaskList(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)  # By default it's not done, because i made it false

    def __str__(self):
        return self.task + " - " + str(self.done)  ## str because its boolean
