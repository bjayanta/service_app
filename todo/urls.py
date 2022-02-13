from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="todo.index"),
    path('create/', views.create, name="todo.create"),
    path('store/', views.store, name="todo.store"),
    path('show/<int:id>', views.show, name="todo.show"),
    path('edit/<int:id>', views.edit, name="todo.edit"),
    path('update/<int:id>', views.update, name="todo.update"),
    path('delete/<int:id>', views.delete, name="todo.delete"),
]
