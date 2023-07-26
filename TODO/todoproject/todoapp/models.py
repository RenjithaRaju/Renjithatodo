from django.db import models

# Create your models here.

class Todosign(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField()
    
class usertask(models.Model):
    userimage=models.ImageField(upload_to='userimage',null=False,blank=True) 
    tasks=models.CharField(max_length=200,default='')
    percentages=models.CharField(max_length=200,default='')
    dates=models.CharField(max_length=200,default='')

