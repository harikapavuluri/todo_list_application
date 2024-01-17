from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
class PositionForm(forms.Form):
    position = forms.CharField()

class TaskForm(forms.ModelForm):
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]

    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, initial='medium')

    class Meta:
        model = Task
        fields = ['title', 'description', 'complete', 'priority', 'due_date']

    def save(self, commit=True):
        # Get the instance of the task
        instance = super(TaskForm, self).save(commit=False)

        # Check if due_date is provided
        if not self.cleaned_data['due_date']:
            # If due_date is blank, set it to None
            instance.due_date = None

        if commit:
            instance.save()

        return instance



