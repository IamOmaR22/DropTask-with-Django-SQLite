from django.db import models

# Create your models here.

class TaskList(models.Model):
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)  # By default it's not done, because i made it false

    def __str__(self):
        return self.task + " - " + str(self.done)  ## str because its boolean
