from rest_framework import serializers

from locations.models import Location
from suppliers.companies.models import Company
from suppliers.models import Supplier


class CompanySerializer(serializers.ModelSerializer):
    location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all())
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())

    class Meta:
        model = Company
        fields = ['id', 'title', 'description', 'location', 'supplier']