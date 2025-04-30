from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Role(models.Model):
    name= models.CharField(max_length=255)
    description = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='role')
    
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='task')
    
    def __str__(self):
        return self.title

class Achievement(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='achievement')
    
    def __str__(self):
        return self.title
