from django.shortcuts import render
from rest_framework import viewsets

from services.car_service.models import CarService
from services.car_service.serializers import CarServiceSerializer


class CarServiceViewSet(viewsets.ModelViewSet):
    queryset = CarService.objects.all()
    serializer_class = CarServiceSerializer