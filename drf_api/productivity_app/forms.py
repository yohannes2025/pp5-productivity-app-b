# forms.py
from django import forms
from .models import Task, Attachment, User, Settings

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'category', 'assigned_users']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ['color_theme', 'calendar_start_day', 'notification_settings']
