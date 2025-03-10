# todos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),  # GET /todos/
    path('todos/<int:id>/', views.todo_detail, name='todo_detail'),  # GET /todos/:id
    path('todos/new/', views.create_todo, name='create_todo'),  # POST /todos/
    path('todos/<int:id>/delete/', views.delete_todo, name='delete_todo'),  # DELETE /todos/:id/delete
]
