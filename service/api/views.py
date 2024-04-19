from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from api.models import MicroServico
from api.serializers import MicroServicoSerializer

class MicroServicoViewSet(viewsets.ModelViewSet):
    serializer_class = MicroServicoSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['codigo']
    queryset = MicroServico.objects.all()

