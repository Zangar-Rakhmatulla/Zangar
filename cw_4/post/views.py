# post/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Post
from .forms import ThreadForm, PostForm

# Главная страница
def index(request):
    return redirect('thread_list')

# Список всех Threads
def thread_list(request):
    threads = Thread.objects.all()
    return render(request, 'post/thread_list.html', {'threads': threads})

# Детали Thread с постами
def thread_detail(request, id):
    thread = get_object_or_404(Thread, id=id)
    posts = Post.objects.filter(thread=thread)
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.thread = thread
            post.save()
            return redirect('thread_detail', id=id)
    else:
        post_form = PostForm()
    return render(request, 'post/thread_detail.html', {'thread': thread, 'posts': posts, 'post_form': post_form})

# Редактирование существующего Thread или создание нового
def thread_edit(request, id=None):
    if id:  # Если передан id, значит редактируем существующий Thread
        thread = get_object_or_404(Thread, id=id)
    else:  # Если id не передан, создаем новый Thread
        thread = None

    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('thread_list')  # После успешного сохранения перенаправляем на список всех threads
    else:
        form = ThreadForm(instance=thread)

    return render(request, 'post/thread_edit.html', {'form': form, 'thread': thread})

# Удаление Thread
def thread_delete(request, id):
    thread = get_object_or_404(Thread, id=id)
    thread.delete()
    return redirect('thread_list')

# Удаление Post
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    thread_id = post.thread.id  # Запоминаем id thread для перенаправления
    post.delete()
    return redirect('thread_detail', id=thread_id)

# Редактирование Post
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', id=post.thread.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'post/post_edit.html', {'form': form, 'post': post})
