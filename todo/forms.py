from tkinter import Widget
from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    
    class Meta:
        model = Todo
        fields = ['label', 'status', 'reminder']
        widgets = {
            'reminder': forms.DateTimeInput(attrs={'value': '2006-10-25 14:30:59'})
        }
