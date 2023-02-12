"""
Views for the user API.
"""
from django.contrib.auth import get_user_model
from rest_framework import filters, permissions
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveUpdateAPIView)
from user.serializers import UserSerializer
from patrimonio.models import Patrimonio
from patrimonio.serializers import PatrimonioSerializer


class UserViewSet(ReadOnlyModelViewSet):
    """Lists users in the system."""
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'id']
    ordering = ['name']


class CreateUserView(CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'id']
    ordering = ['name']


class ManageUserView(RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'id']
    ordering = ['name']

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user


class UserPatrimonioListView(ListAPIView):
    """Return a list of all Patrimonio objects related to a user."""
    queryset = Patrimonio.objects.all()
    serializer_class = PatrimonioSerializer

    def get_queryset(self):
        user = get_user_model().objects.get(id=self.kwargs.get('id'))
        return self.queryset.filter(responsavel=user)
