"""
Core views for app.
"""
import json

from core.serializers import GroupSerializer
from django.contrib.auth.models import Group
from django.http import JsonResponse
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet


class GroupViewSet(ReadOnlyModelViewSet):
    """Manage ingredients in the database."""
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = [IsAdminUser]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'id']
    ordering = ['name']


@api_view(['GET'])
def health_check(request):
    """Returns successful response."""
    return Response({'healthy': True})


@api_view(['GET'])
def habilitacao(request):
    """Returns dados de habilitação."""
    with open("../../vol/web/media/json/habilitacao.json") as json_file:
        json_data = json.load(json_file)
    return JsonResponse(json_data)


@api_view(['GET'])
def a(request):
    """Returns critério A data."""
    with open("../../vol/web/media/json/a.json") as json_file:
        json_data = json.load(json_file)
    return JsonResponse(json_data)


@api_view(['GET'])
def b(request):
    """Returns critério B data."""
    with open("../../vol/web/media/json/b.json") as json_file:
        json_data = json.load(json_file)
    return JsonResponse(json_data)


@api_view(['GET'])
def c(request):
    """Returns critério C data."""
    with open("../../vol/web/media/json/c.json") as json_file:
        json_data = json.load(json_file)
    return JsonResponse(json_data)


@api_view(['GET'])
def d(request):
    """Returns critério D data."""
    with open("../../vol/web/media/json/d.json") as json_file:
        json_data = json.load(json_file)
    return JsonResponse(json_data)


@api_view(['GET'])
def e(request):
    """Returns critério E data."""
    with open("../../vol/web/media/json/e.json") as json_file:
        json_data = json.load(json_file)
    return JsonResponse(json_data)


@api_view(['GET'])
def f(request):
    """Returns critério F data."""
    with open("../../vol/web/media/json/f.json") as json_file:
        json_data = json.load(json_file)
    return JsonResponse(json_data)


@api_view(['GET'])
def g(request):
    """Returns critério G data."""
    with open("../../vol/web/media/json/g.json") as json_file:
        json_data = json.load(json_file)
    return JsonResponse(json_data)


@api_view(['GET'])
def h(request):
    """Returns critério H data."""
    with open("../../vol/web/media/json/h.json") as json_file:
        json_data = json.load(json_file)
    return JsonResponse(json_data)


@api_view(['GET'])
def i(request):
    """Returns critério I data."""
    with open("../../vol/web/media/json/i.json") as json_file:
        json_data = json.load(json_file)
    return JsonResponse(json_data)
