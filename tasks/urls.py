from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'priorities', views.PriorityViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'states', views.StateViewSet)
router.register(r'tasks', views.TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]
