from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="todo.index"),
    path('create/', views.create, name="todo.create"),
    path('store/', views.store, name="todo.store"),
]
