from django.db import models


# Create your models here.
class Environment(models.Model):
    '''
    The `Environment` model represents an individual reinforcement learning task.
    '''
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    video_url = models.URLField()
