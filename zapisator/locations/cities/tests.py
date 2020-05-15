from rest_framework import status
from rest_framework.test import APITestCase

from locations.cities.models import City

CITIES_URL = '/cities/'


class CityTests(APITestCase):

    def test_create_city(self):
        """
        Создание города
        """
        data = {
            'title': 'Екатеринбург'
        }

        response = self.client.post(CITIES_URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(City.objects.get().title, 'Екатеринбург')
