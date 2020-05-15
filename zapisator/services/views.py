from rest_framework import viewsets, mixins

from services.models import Service
from services.serializers import ServiceSerializer


class ServiceViewSet(mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
