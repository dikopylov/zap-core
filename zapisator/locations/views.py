from rest_framework import viewsets

from locations.cities.serializers import CitySerializer
from locations.models import Location
from locations.serializers import LocationSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
