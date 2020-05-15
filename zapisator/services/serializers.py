from rest_framework import serializers

from services.models import Service
from suppliers.companies.models import Company


class ServiceSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())

    class Meta:
        model = Service
        fields = '__all__'
        ordering = ['-id']
