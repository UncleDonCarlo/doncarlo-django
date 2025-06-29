from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('admin', admin.site.urls),

    path('api/schema', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/swagger', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('api/projects', include('interfaces.project.urls')),
    path('api/tasks', include('interfaces.task.urls')),



    path('api/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
