"""
Serializers for core APIs
"""
from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import (
    Group,
)
from django.contrib.auth import (
    get_user_model,
)
from patrimonio.models import Patrimonio


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'name', 'email']


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class PatrimonioSerializer(ModelSerializer):

    # responsavel = UserSerializer
    # setor = GroupSerializer

    class Meta:
        model = Patrimonio
        fields = ['tipo', 'marca', 'modelo', 'responsavel', 'setor']
