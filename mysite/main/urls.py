"""
in here we gooan define paths
to select for respective view
"""
from django.urls import path
from . import views
#starting page path with ""
urlpatterns = [
    path("",views.index, name="index"),
    path("v1/",views.v1, name="view 1"),
]
