from rest_framework import viewsets

from locations.cities.models import City
from locations.cities.serializers import CitySerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
