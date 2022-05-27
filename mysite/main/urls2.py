"""
urls2
/id/.....
"""
from django.urls import path
from . import views
urlpatterns = [
    path("<int:idValue>",views.id, name="id"),#enter todolist id
    path("<int:idValue>/pending",views.pending,name="pending"),
    path("<int:idValue>/completed",views.completed,name="done"),
]
