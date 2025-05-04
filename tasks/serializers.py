from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task, Priority, Category, State


class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    assigned_to = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True, required=False)
    priority = PrioritySerializer(read_only=True)
    priority_id = serializers.PrimaryKeyRelatedField(queryset=Priority.objects.all(
    ), source='priority', write_only=True, allow_null=True, required=False)
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(
    ), source='category', write_only=True, allow_null=True, required=False)
    state = StateSerializer(read_only=True)
    state_id = serializers.PrimaryKeyRelatedField(queryset=State.objects.all(
    ), source='state', write_only=True, allow_null=True, required=False)
    attachment = serializers.FileField(required=False, allow_null=True)

    class Meta:
        model = Task
        fields = '__all__'
