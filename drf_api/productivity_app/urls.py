# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('tasks/', views.task_list_view, name='task_list'),
    path('tasks/<int:task_id>/', views.task_detail_view, name='task_detail'),
    path('tasks/create/', views.task_create_view, name='task_create'),
    path('tasks/<int:task_id>/edit/', views.task_edit_view, name='task_edit'),
    path('profile/', views.user_profile_view, name='user_profile'),
    path('settings/', views.settings_view, name='settings'),
]

