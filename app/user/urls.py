"""
URL mappings for the user API.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user.views import (CreateUserView, ManageUserView,
                        UserPatrimonioListView, UserViewSet)

app_name = 'user'

router = DefaultRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', CreateUserView.as_view(), name='create'),
    path('me/', ManageUserView.as_view(), name='me'),

    path('<int:id>/patrimonio/',
         UserPatrimonioListView.as_view(),
         name='user-patrimonio-list'),
]
