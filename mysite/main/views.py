"""
site views
can create multiple views here.
"""
from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def index(response):
    "home page"
    return HttpResponse("<h1>Saravanan Ramanathan</h1>")

def v1(response):
    "view1"
    return HttpResponse("<h1>View1!</h1>")