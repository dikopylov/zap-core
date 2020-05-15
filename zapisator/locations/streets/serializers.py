from rest_framework import serializers

from locations.cities.models import City
from locations.streets.models import Street


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ['id', 'title', 'house']
