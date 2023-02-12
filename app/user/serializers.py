"""
Serializers for the user API View.
"""
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from patrimonio.models import Patrimonio
# from django.utils.translation import gettext as _


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class PatrimonioSerializer(ModelSerializer):
    class Meta:
        model = Patrimonio
        fields = ['id', 'tipo', 'marca', 'modelo']


class UserSerializer(ModelSerializer):
    """Serializer for the user object."""

    groups = SerializerMethodField()
    patrimonios = SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ['email', 'password', 'name', 'id', 'groups', 'patrimonios']
        # read_only_fields = ['email']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def get_groups(self, user):
        """Return the list of groups assigned to the user."""
        groups = user.groups.all()
        return GroupSerializer(groups, many=True).data

    def get_patrimonios(self, user):
        """Return the list of patrimonios assigned to the user."""
        patrimonios = Patrimonio.objects.filter(responsavel=user.id)
        return PatrimonioSerializer(patrimonios, many=True).data

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update and return user."""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user
