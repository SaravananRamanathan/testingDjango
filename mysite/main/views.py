"""
site views
can create multiple views here.
"""
from pyexpat import model
from django.shortcuts import render
from django.http.response import HttpResponse

from . import models
# Create your views here.

def index(response):
    "home page"
    return HttpResponse("<h1>testing by srvnn %s</h1>"%id)
def id(response,idValue:int):
    print("testing id")
    t=models.ToDoList;
    item=t.objects.get(id=idValue).item_set.get(id=1)
    #print(t.objects.get(id=idValue))
    return HttpResponse(f"<h1>The value for id {idValue} is:</h1>\
        <h2>{t.objects.get(id=idValue).name}</h2>\
                 <p>{item.text}={item.complete}<p>")