from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    # Add any additional user-related fields here
    # bio = models.TextField(blank=True)
    # location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username
