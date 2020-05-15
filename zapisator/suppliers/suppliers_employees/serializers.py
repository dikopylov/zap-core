from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.serializers import UserSerializer
from suppliers.suppliers_employees.models import SupplierEmployee


class SupplierEmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = SupplierEmployee
        fields = ['user', 'company']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_model = get_user_model().objects.create(**user_data)

        return SupplierEmployee.objects.create(user=user_model, **validated_data)
