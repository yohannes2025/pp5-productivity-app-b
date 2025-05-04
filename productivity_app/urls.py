# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from tasks import views
# from django.contrib import admin

# router = DefaultRouter()
# router.register(r'priorities', views.PriorityViewSet)
# router.register(r'categories', views.CategoryViewSet)
# router.register(r'states', views.StateViewSet)
# router.register(r'tasks', views.TaskViewSet, basename='task')

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("api/", include("tasks.urls")),
#     path('', include(router.urls)),
# ]

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Productivity App API",
        default_version='v1',
        description="API for the Productivity App",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tasks/', include('tasks.urls')),
    path('api/users/', include('users.urls')),  # Include users app URLs
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
