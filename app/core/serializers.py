"""
Serializers for core APIs
"""
from rest_framework import serializers

from django.contrib.auth.models import (
    Group,
)
from django.contrib.auth import (
    get_user_model,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'name', 'email']


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for Groups."""
    users = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions', 'users']
        read_only_fields = ['id']

    def get_users(self, group):
        """Return the list of users assigned to the group."""
        users = group.user_set.all()
        return UserSerializer(users, many=True).data
