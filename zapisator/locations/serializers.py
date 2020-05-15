from rest_framework import serializers

from locations.cities.models import City
from locations.cities.serializers import CitySerializer
from locations.models import Location
from locations.streets.models import Street
from locations.streets.serializers import StreetSerializer
from suppliers.companies.models import Company


class LocationSerializer(serializers.ModelSerializer):
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())
    street = serializers.PrimaryKeyRelatedField(queryset=Street.objects.all())

    class Meta:
        model = Location
        fields = ['id', 'city', 'street']
