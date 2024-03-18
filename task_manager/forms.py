from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'priority']

    title = forms.CharField(label="What's the Task?", max_length=250)
    due_date = forms.DateField(label='Due Date', widget=forms.DateInput(attrs={'type': 'date'}))
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    priority = forms.ChoiceField(label='Priority', choices=PRIORITY_CHOICES)
