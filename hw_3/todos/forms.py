# todos/forms.py
from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'status']

    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']  # Убедитесь, что формат правильный
    )
