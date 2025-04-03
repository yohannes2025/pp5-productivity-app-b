from rest_framework import serializers
from .models import User, Task, Attachment

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model."""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class AttachmentSerializer(serializers.ModelSerializer):
    """Serializer for the Attachment model."""
    class Meta:
        model = Attachment
        fields = ['id', 'task', 'file', 'created_at']

class TaskSerializer(serializers.ModelSerializer):
    """Serializer for the Task model."""
    assigned_users = UserSerializer(many=True, read_only=True)
    attachments = AttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority', 'category', 'assigned_users', 'is_complete', 'created_at', 'updated_at', 'attachments']
