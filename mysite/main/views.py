"""
site views
can create multiple views here.
"""
from pyexpat import model
from django.shortcuts import render
from django.http.response import HttpResponse

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

"""
#old method
def id(response,idValue:int):
    print("testing id")
    t=models.ToDoList;
    items=t.objects.get(id=idValue).item_set.all()
    #print(t.objects.get(id=idValue))
    text1=f"<h1>The value for id {idValue} is:</h1>\
        <h2>{t.objects.get(id=idValue).name}</h2>"
    text2=""
    if(not items.exists()):
        text2="<p>no items found.<p>"
    print(f"checking stuff: {items}")
    
    for i in items:
        text2+=f"<p>{i.text}={i.complete}<p>"
    return HttpResponse(text1+text2)
"""
