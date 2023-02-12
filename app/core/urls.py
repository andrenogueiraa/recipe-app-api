"""
URL mappings for the recipe app.
"""
from django.urls import (
    path,
    include,
)
from rest_framework.routers import DefaultRouter
from .views import a, b, c, d, e, f, g, h, i, habilitacao, GroupViewSet


router = DefaultRouter()
router.register('groups', GroupViewSet)

app_name = 'core'

urlpatterns = [
    path('', include(router.urls)),
    path('criterios/habilitacao', habilitacao),
    path('criterios/a', a),
    path('criterios/b', b),
    path('criterios/c', c),
    path('criterios/d', d),
    path('criterios/e', e),
    path('criterios/f', f),
    path('criterios/g', g),
    path('criterios/h', h),
    path('criterios/i', i),
]
