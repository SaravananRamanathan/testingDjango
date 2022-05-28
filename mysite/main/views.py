"""
site views
can create multiple views here.
"""
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import CreateNewList
from . import models
# Create your views here.

def home(response):
    "home page"
    #return HttpResponse("<h1>testing- srvnn %s</h1>"%id)
    return render(response,"main/home.html",{})

todolist = None

def id(response,idValue:int):
    "displaying all of todolist"
    global todolist 
    todolist = models.ToDoList.objects.get(id=idValue)    
    return render(response,"main/lists.html",{"data":todolist})

def pending(response,idValue:int):
    "only display pending tasks from todolist"
    global todolist 
    todolist = models.ToDoList.objects.get(id=idValue)
    print(f"testing pending url, received id: {idValue}")
    return render(response,"main/listPending.html",{"data":todolist})

def completed(response,idValue:int):
    "only display completed tasks from todolist"
    global todolist 
    todolist = models.ToDoList.objects.get(id=idValue)
    print(f"testing compelted, received id: {idValue} ")
    return render(response,"main/listCompleted.html",{"data":todolist})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            "if data entererd in form is valid"
            #n=form.cleaned_data["name"]
            #print(form.cleaned_data)#{'name': 'tada', 'check': True}
            

        return HttpResponseRedirect("/") #just "/" to redirect to home page 
    else:    
        form=CreateNewList()
    return render(response,"main/create.html",{"form":form})