"""
site views
can create multiple views here.
"""
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
    #todolist = models.ToDoList.objects.raw(f"SELECT *,row_number() OVER(ORDER BY Id) AS sno FROM main_todolist WHERE id={idValue}")#.filter(id=idValue)
    todolist = models.ToDoList.objects.filter(id=idValue)
    print(todolist)
    if response.method=="POST":
        ""
        print(response.POST)
        if response.POST.get("save"):
            ""
            print("testing save button")
        elif response.POST.get("newItem"):
            ""
            print("testing get button")
    class sendToTemplate:
        temp=0
        def num(self,):
            self.temp+=1
            return self.temp
    #data=sendToTemplate()
    #print(f"testing items: {todolist[0].item_set.all().count()}")  
    #testingLists.html -- new mthod custom forms/advaned forms
    #lists.html -- old method with basic forms
    return render(response,"main/testingLists.html",{"list":todolist,"id":idValue,"sno":sendToTemplate()})

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
            return HttpResponseRedirect("/display") #just "/" to redirect to home page 
    else:    
        form=CreateNewList()
    return render(response,"main/createList.html",{"form":form})

def display(response):
    #todolist = models.ToDoList.objects.all()
    todolist = models.ToDoList.objects.raw("SELECT *,row_number() OVER(ORDER BY Id) AS ROWNUM FROM main_todolist")
        #print(i.ROWNUM)
    return render(response,"main/display.html",{"data":todolist})

def delete(response):
    temp = models.ToDoList.objects.all()
    max_id=0
    for i in temp:
        max_id=i.id
    
    if response.method=="POST":
        form1 = DeleteList(max_id,response.POST)
        if form1.is_valid():
            "if valid input , then delete that id"
            temp.filter(id=form1.cleaned_data["id"]).delete()
            
            return HttpResponseRedirect("/display")
    else:
        form1 = DeleteList(max_id)
    return render(response,"main/deleteList.html",{"form":form1})