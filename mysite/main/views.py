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
    return render(response,"main/navbar.html",{})


def id(response,idValue:int):
    "displaying all of todolist"
    #todolist = models.ToDoList.objects.raw(f"SELECT *,row_number() OVER(ORDER BY Id) AS sno FROM main_todolist WHERE id={idValue}")#.filter(id=idValue)
    todolist = models.ToDoList.objects.filter(id=idValue)
    print(todolist)
    if response.method=="POST":
        ""
        print(f'testing response: {response.POST}')
        if response.POST.get("save"):
            ""
            print("testing save button")
            if todolist[0].item_set.all().exists():
                for i in todolist[0].item_set.all():
                    if response.POST.get('c'+str(i.id)):
                        ""
                        print("checked case")
                        i.complete=True
                        #print(f"{i.complete} {i.text}")
                        #print(f"{'c'+str(i.id)}={response.POST.get('c'+str(i.id))}")
                    else:
                        print("not checked")
                        i.complete=False
                        #print(f"{i.complete} {i.text}")
                        #print(f"{'c'+str(i.id)}={response.POST.get('c'+str(i.id))}")
                    i.save()
        elif response.POST.get("newItem"):
            ""
            print("testing newItem button")
            itemName:str= response.POST.get("itemName")
            print(f"New item name:{itemName}.")
            if not itemName.isspace():
                if len(itemName)>0:
                    if itemName[0]!=' ':
                        #print("elibible")        
                        todolist[0].item_set.create(text=itemName,complete=False)
            #todolist[0].item_set.create(text=itemName,complete=False)


    class sendToTemplate:
        temp=0
        def num(self,):
            self.temp+=1
            return self.temp
    #data=sendToTemplate()
    #print(f"testing items: {todolist[0].item_set.all().count()}")  
    #testingLists.html -- new mthod custom forms/advaned forms
    #lists.html -- old method with basic forms
    return render(response,"main/listsDesigns1.html",{"list":todolist,"id":idValue,"sno":sendToTemplate()})

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
    #TODO: this display function probs will fail if there is no data in list.
    todolist = models.ToDoList.objects.raw("SELECT *,row_number() OVER(ORDER BY Id) AS ROWNUM FROM main_todolist")
        #print(i.ROWNUM)
    return render(response,"main/displayDesigns1.html",{"data":todolist})

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