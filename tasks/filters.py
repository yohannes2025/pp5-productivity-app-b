import django_filters
from .models import Task, Priority, Category, State
from django.contrib.auth.models import User


class TaskFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    due_date = django_filters.DateTimeFilter()
    due_date__gt = django_filters.DateTimeFilter(
        field_name='due_date', lookup_expr='gt')
    due_date__lt = django_filters.DateTimeFilter(
        field_name='due_date', lookup_expr='lt')
    is_overdue = django_filters.BooleanFilter()
    priority = django_filters.ModelChoiceFilter(
        queryset=Priority.objects.all())
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all())
    state = django_filters.ModelChoiceFilter(queryset=State.objects.all())
    owner = django_filters.ModelChoiceFilter(queryset=User.objects.all())
    assigned_to = django_filters.ModelMultipleChoiceFilter(
        queryset=User.objects.all())

    class Meta:
        model = Task
        fields = ['title', 'due_date', 'is_overdue', 'priority',
                  'category', 'state', 'owner', 'assigned_to']
