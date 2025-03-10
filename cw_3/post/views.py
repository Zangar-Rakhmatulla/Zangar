# post/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Thread, Post
from .forms import ThreadForm, PostForm

# Главная страница, перенаправление на /threads
def index(request):
    return redirect('thread_list')

# Страница с списком всех тредов
def thread_list(request):
    threads = Thread.objects.all()
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thread_list')
    else:
        form = ThreadForm()
    return render(request, 'post/thread_list.html', {'threads': threads, 'form': form})

# Страница для просмотра подробностей о треде и постах
def thread_detail(request, id):
    thread = get_object_or_404(Thread, id=id)
    posts = Post.objects.filter(thread=thread)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.save()
            return redirect('thread_detail', id=thread.id)
    else:
        form = PostForm()
    return render(request, 'post/thread_detail.html', {'thread': thread, 'posts': posts, 'form': form})

# Удаление треда
def delete_thread(request, id):
    thread = get_object_or_404(Thread, id=id)
    thread.delete()
    return redirect('thread_list')

# Редактирование треда
def edit_thread(request, id):
    thread = get_object_or_404(Thread, id=id)
    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', id=thread.id)
    else:
        form = ThreadForm(instance=thread)
    return render(request, 'post/edit_thread.html', {'form': form})

# Удаление поста
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('thread_detail', id=post.thread.id)

# Редактирование поста
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', id=post.thread.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'post/edit_post.html', {'form': form})
