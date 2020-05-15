from rest_framework import status
from rest_framework.test import APITestCase

from suppliers.companies.models import Company

CAR_SERVICES_URL = '/car-services/'


class CarServiceTests(APITestCase):

    def test_create_car_service(self):
        """
        Создание авто услуги
        """

        data = {
            'service': {
                'title': 'Мойка',
                'description': 'Экспресс',
                'price': 999.99,
                'duration': '10:30',
                'company': 1
            },
        }

        Company.objects.create(pk=1)

        response = self.client.post(CAR_SERVICES_URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)