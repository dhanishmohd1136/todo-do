# todo_project/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

# Swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Todo API",
        default_version='v1',
        description="Todo API Documentation",
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    
    path('admin/', admin.site.urls),

    # API
    path('api/', include('todo.urls')),

    # Auth Token
    path('api/token/', obtain_auth_token),

    # Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
]