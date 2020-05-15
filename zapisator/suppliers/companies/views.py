from rest_framework import viewsets

from suppliers.companies.models import Company
from suppliers.companies.serializers import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
