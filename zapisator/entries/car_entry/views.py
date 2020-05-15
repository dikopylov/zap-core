from rest_framework import viewsets

from entries.car_entry.filters import CarEntryFilter
from entries.car_entry.models import CarEntry
from entries.car_entry.serializers import CarEntrySerializer


class CarEntryViewSet(viewsets.ModelViewSet):
    queryset = CarEntry.objects.all()
    serializer_class = CarEntrySerializer
    filter_class = CarEntryFilter
