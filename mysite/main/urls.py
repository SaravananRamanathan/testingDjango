"""
in here we gooan define paths
to select for respective view
"""
from django.urls import path
from . import views
#starting page path with ""
urlpatterns = [
    path("",views.home, name="home"),#home page
    path("create/",views.create,name="createList"),
    path("display/",views.display,name="displayList"),
    path("delete/",views.delete,name="deleteList")
]
