# views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Attachment
from .forms import TaskForm, UserProfileForm, SettingsForm
from .models import MyModel


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

def index(request):
    return render(request, 'index.html')

@login_required
def calendar_view(request):
    """View for the calendar display."""
    tasks = Task.objects.filter(assigned_users__in=[request.user])
    context = {
        'tasks': tasks,
        'current_date': datetime.now(),
    }
    return render(request, 'calendar.html', context)

@login_required
def task_list_view(request):
    """View for the task list display."""
    tasks = Task.objects.filter(assigned_users__in=[request.user])
    if request.GET.get('category'):
        tasks = tasks.filter(category=request.GET.get('category'))
    if request.GET.get('status'):
        tasks = tasks.filter(is_complete=request.GET.get('status') == 'complete')
    if request.GET.get('due_date'):
        tasks = tasks.filter(due_date=request.GET.get('due_date'))
    if request.GET.get('assigned_to'):
        tasks = tasks.filter(assigned_users__in=[request.GET.get('assigned_to')])
    if request.GET.get('search'):
        tasks = tasks.filter(title__icontains=request.GET.get('search'))
    tasks = tasks.order_by('due_date', 'priority')
    context = {
        'tasks': tasks,
    }
    return render(request, 'task_list.html', context)

@login_required
def task_detail_view(request, task_id):
    """View for the task detail display."""
    task = get_object_or_404(Task, id=task_id, assigned_users__in=[request.user])
    if request.method == 'POST':
        if 'complete' in request.POST:
            task.is_complete = True
            task.save()
    context = {
        'task': task,
    }
    return render(request, 'task_detail.html', context)

@login_required
def task_create_view(request):
    """View for creating a new task."""
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.assigned_users.add(request.user)
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

@login_required
def task_edit_view(request, task_id):
    """View for editing an existing task."""
    task = get_object_or_404(Task, id=task_id, assigned_users__in=[request.user])
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

@login_required
def user_profile_view(request):
    """View for the user profile page."""
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'user_profile.html', {'form': form})

@login_required
def settings_view(request):
    """View for the user settings page."""
    if request.method == 'POST':
        form = SettingsForm(request.POST, instance=request.user.settings)
        if form.is_valid():
            form.save()
            return redirect('settings')
    else:
        form = SettingsForm(instance=request.user.settings)
    return render(request, 'settings.html', {'form': form})

