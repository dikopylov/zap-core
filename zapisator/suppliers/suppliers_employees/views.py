from rest_framework import viewsets

from suppliers.suppliers_employees.models import SupplierEmployee
from suppliers.suppliers_employees.serializers import SupplierEmployeeSerializer
from users.serializers import UserSerializer


class SupplierEmployeeViewSet(viewsets.ModelViewSet):
    queryset = SupplierEmployee.objects.all()
    serializer_class = SupplierEmployeeSerializer
    user_serializer = UserSerializer
