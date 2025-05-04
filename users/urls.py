from django.urls import path
# Make sure UserDetailView is imported here
from .views import UserRegistrationView, UserDetailView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('<int:pk>/', UserDetailView.as_view(),
         name='user-detail'),  # This handles /api/users/1/
    # Add other user-related URLs as needed
]
