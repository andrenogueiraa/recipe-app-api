from core import views as core_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/health-check/', core_views.health_check, name='health-check'),
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='api-schema'),
        name='api-docs',
    ),
    # path('api/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/users/', include('user.urls')),
    path('api/', include('recipe.urls')),
    path('api/', include('core.urls')),
    path('api/', include('patrimonio.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
