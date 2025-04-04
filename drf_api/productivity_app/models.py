# models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


# class MyModel(models.Model):
#     """
#     This is a sample model that represents a basic entity in your application.
#     You can customize the fields and add more models as per your requirements.
#     """
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name

class User(AbstractUser):
    # Your additional fields would go here
    
    # Define the groups relationship with a unique related_name
    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='custom_user_set',  # Change this to a unique name
        help_text='The groups this user belongs to. A user will get all permissions '
                  'granted to each of their groups.',
        verbose_name='groups'
    )

    # Define the user_permissions relationship with a unique related_name
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='custom_user_permissions_set',  # Change this to a unique name
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

class Task(models.Model):
    """Model for user tasks."""
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    priority = models.IntegerField(default=1)
    category = models.CharField(max_length=50, blank=True)
    assigned_users = models.ManyToManyField(User, related_name='tasks')
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Attachment(models.Model):
    """Model for task attachments."""
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='attachments/')
    created_at = models.DateTimeField(auto_now_add=True)

class Settings(models.Model):
    """Model for user settings."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='settings')
    color_theme = models.CharField(max_length=50, default='light')
    calendar_start_day = models.IntegerField(default=0)  # 0 for Sunday, 1 for Monday, etc.
    notification_settings = models.JSONField(default=dict)