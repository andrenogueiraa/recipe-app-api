"""
Views for the recipe APIs
"""
from core.models import Ingredient, Recipe, Tag
from drf_spectacular.utils import (OpenApiParameter, OpenApiTypes,
                                   extend_schema, extend_schema_view)
from recipe import serializers
from rest_framework import mixins, status, viewsets
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import (IsAdminUser, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework import filters


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                'tags',
                OpenApiTypes.STR,
                description='Comma separated list of tag IDs to filter',
            ),
            OpenApiParameter(
                'ingredients',
                OpenApiTypes.STR,
                description='Comma separated list of ingredient IDs to filter',
            ),
        ]
    )
)
class RecipeViewSet(ReadOnlyModelViewSet):
    """View for manage recipe APIs."""
    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title', 'id']
    ordering = ['title']

    # def _params_to_ints(self, qs):
    #     """Convert a list of strings to integers."""
    #     return [int(str_id) for str_id in qs.split(',')]

    # def get_queryset(self):
    #     """Retrieve recipes for authenticated user."""
    #     tags = self.request.query_params.get('tags')
    #     ingredients = self.request.query_params.get('ingredients')
    #     queryset = self.queryset
    #     if tags:
    #         tag_ids = self._params_to_ints(tags)
    #         queryset = queryset.filter(tags__id__in=tag_ids)
    #     if ingredients:
    #         ingredient_ids = self._params_to_ints(ingredients)
    #         queryset = queryset.filter(ingredients__id__in=ingredient_ids)

    #     return queryset.filter(
    #         user=self.request.user
    #     ).order_by('-id').distinct()

    # def get_serializer_class(self):
    #     """Return the serializer class for request."""
    #     if self.action == 'list':
    #         return serializers.RecipeSerializer
    #     elif self.action == 'upload_image':
    #         return serializers.RecipeImageSerializer

    #     return self.serializer_class

    # def perform_create(self, serializer):
    #     """Create a new recipe."""
    #     serializer.save(user=self.request.user)

    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        """Upload an image to recipe."""
        recipe = self.get_object()
        serializer = self.get_serializer(recipe, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                'assigned_only',
                OpenApiTypes.INT, enum=[0, 1],
                description='Filter by items assigned to recipes.',
            ),
        ]
    )
)
class BaseRecipeAttrViewSet(mixins.DestroyModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    """Base viewset for recipe attributes."""
    permission_classes = [IsAuthenticatedOrReadOnly]
    # def get_queryset(self):
    #     """Filter queryset to authenticated user."""
    #     assigned_only = bool(
    #         int(self.request.query_params.get('assigned_only', 0))
    #     )
    #     queryset = self.queryset
    #     if assigned_only:
    #         queryset = queryset.filter(recipe__isnull=False)

    #     return queryset.filter(
    #         user=self.request.user
    #     ).order_by('-name').distinct()


class TagViewSet(ReadOnlyModelViewSet):
    """Manage tags in the database."""
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'id']
    ordering = ['name']


class IngredientViewSet(ReadOnlyModelViewSet):
    """Manage ingredients in the database."""
    serializer_class = serializers.IngredientSerializer
    queryset = Ingredient.objects.all()
    permission_classes = [IsAdminUser]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name', 'id']
    ordering = ['name']
