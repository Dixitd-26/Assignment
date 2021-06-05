from django.db import models
from django.db import models

# Create your models here.
class Task(models.Model):
    projectname = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    description = models.CharField(max_length=200)
    duration= models.DateTimeField()
    objects = models.Manager()

    def __str__(self):
        return self.projectname
