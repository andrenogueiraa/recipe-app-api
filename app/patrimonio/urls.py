"""
URL mappings for the recipe app.
"""
from django.urls import include, path
from patrimonio.views import PatrimonioViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('patrimonio', PatrimonioViewSet)

app_name = 'patrimonio'

urlpatterns = [
    path('', include(router.urls)),
]
