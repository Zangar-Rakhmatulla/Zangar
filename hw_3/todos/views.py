# todos/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import TodoForm
from django.http import JsonResponse

# Отображение всех задач
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})

# Отображение задачи по ID
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id)
    return render(request, 'todos/todo_detail.html', {'todo': todo})

# Создание новой задачи
def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todos/create_todo.html', {'form': form})

# Удаление задачи по ID
def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('todo_list')
