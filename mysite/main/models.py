"""
database modles
modling info-to make it easy to grab info
"""
from django.db import models
from django.forms import CharField

# Create your models here.
class ToDoList(models.Model):
    "database object called ToDoList"
    name=models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList,on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return str(self.text)
