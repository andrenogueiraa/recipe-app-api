from rest_framework.viewsets import ReadOnlyModelViewSet
from patrimonio.models import Patrimonio
from patrimonio.serializers import PatrimonioSerializer


class PatrimonioViewSet(ReadOnlyModelViewSet):
    queryset = Patrimonio.objects.only('tipo', 'marca', 'modelo',
                                       'responsavel', 'setor')
    serializer_class = PatrimonioSerializer
