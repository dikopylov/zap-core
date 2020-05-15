from rest_framework import status
from rest_framework.test import APITestCase

from services.car_service.models import CarService
from services.models import Service

SERVICES_URL = '/services/'


class ServiceTests(APITestCase):

    def test_ds(self):
        """
        Получение всех услуг
        """

        data = {
            'title': 'Мойка',
            'description': 'Экспресс',
            'price': 999.99,
            'duration': "20"
        }

        service = Service.objects.create(**data)

        CarService.objects.create(service=service)

        response = self.client.get(SERVICES_URL, data, format='json')
        links = response.data.pop('links')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.pop('count'), 21)
        self.assertIsNotNone(links)

    def test_get_all_services(self):
        """
        Получение всех услуг
        """

        data = {
            'title': 'Мойка',
            'description': 'Экспресс',
            'price': 999.99,
        }

        service = Service.objects.create(**data)

        for counter in range(1, 22):
            CarService.objects.create(service=service)

        response = self.client.get(SERVICES_URL, data, format='json')
        links = response.data.pop('links')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.pop('count'), 21)
        self.assertIsNotNone(links)
