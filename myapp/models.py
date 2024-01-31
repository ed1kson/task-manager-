from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.username
    
class Task(models.Model):
    taskname = models.CharField(max_length = 100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING, related_name = 'tasks')

    def __str__(self):
        return self.taskname
