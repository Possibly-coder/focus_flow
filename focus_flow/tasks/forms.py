
from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Urgent', '🔥 Blaze Mode'),
    ]

    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, label="Priority", widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Todo
        fields = ['title', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'You wanna rename your task...?'}),
        }
