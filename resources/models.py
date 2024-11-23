from django.db import models

class DeviceResource(models.Model):
    resource_name = models.CharField(max_length=100)  # Name of the resource
    value = models.FloatField()  # Value of the resource (e.g., CPU %)
    timestamp = models.DateTimeField(auto_now_add=True)  # When the data was added

    def __str__(self):
        return f"{self.resource_name}: {self.value}"
    

class Metric(models.Model):
    title = models.CharField(max_length=100)  # e.g., CPU, RAM
    value = models.CharField(max_length=100)  # e.g., '20% usage'
    icon = models.CharField(max_length=100)   # Icon name for frontend (e.g., 'Cpu')

    def __str__(self):
        return self.title

