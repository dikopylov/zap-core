from services.car_service.models import CarService
from services.models import Service
from services.serializers import ServiceSerializer


class CarServiceSerializer(ServiceSerializer):
    service = ServiceSerializer(required=True)

    class Meta:
        model = CarService
        fields = ['service']

    def create(self, validated_data):
        car_service = None
        service_data = validated_data.pop('service', None)

        if service_data is not None:
            service = Service.objects.create(**service_data)
            car_service = CarService.objects.create(service=service, **validated_data)

        return car_service
