from django.db import models

class Log(models.Model):
    '''
    Contains data on response time
    '''
    responseTime = models.CharField(max_length=10000)
