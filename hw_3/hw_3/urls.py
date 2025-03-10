# hw_3/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todos.urls')),  # Включаем маршруты из приложения todos
]
