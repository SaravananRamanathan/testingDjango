"""
site views
can create multiple views here.
"""
from glob import glob
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CreateNewList,DeleteList
from . import models
# Create your views here.

def home(response):
    "home page"
    #return HttpResponse("<h1>testing- srvnn %s</h1>"%id)
    return render(response,"main/home.html",{})


def id(response,idValue:int):
    "displaying all of todolist"
    todolist = models.ToDoList.objects.filter(id=idValue) 
    return render(response,"main/lists.html",{"list":todolist,"id":idValue})

def pending(response,idValue:int):
    "only display pending tasks from todolist"
    todolist = models.ToDoList.objects.filter(id=idValue)
    return render(response,"main/listPending.html",{"list":todolist,"id":idValue})

def completed(response,idValue:int):
    "only display completed tasks from todolist"
    todolist = models.ToDoList.objects.filter(id=idValue)
    return render(response,"main/listCompleted.html",{"list":todolist,"id":idValue})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            "if data entererd in form is valid"
            temp = models.ToDoList(name=form.cleaned_data["name"])
            temp.save()
            print(f"data is valid: {form.cleaned_data}")#{'name': 'tada', 'check': True}
            return HttpResponseRedirect("/display") #just "/" to redirect to home page 
    else:    
        form=CreateNewList()
    return render(response,"main/createList.html",{"form":form})

def display(response):
    todolist = models.ToDoList.objects.all()
    return render(response,"main/display.html",{"data":todolist})

def delete(response):
    if response.method=="POST":
        form1 = DeleteList(10,response.POST)
        print(f"delete button pressed: {form1.is_valid()}")#just checking
        if form1.is_valid():
            ""
            print("valid form: {}".format(form1.cleaned_data))#just checking
            return HttpResponseRedirect("/display")
    else:
        form1 = DeleteList(10) #-- i want to do this...and use a number to set maxVaue of a field
        #form1 = DeleteList()
    return render(response,"main/deleteList.html",{"form":form1})