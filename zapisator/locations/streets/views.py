from rest_framework import viewsets

from locations.streets.models import Street
from locations.streets.serializers import StreetSerializer


class StreetViewSet(viewsets.ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
