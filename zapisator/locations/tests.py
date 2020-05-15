from rest_framework import status
from rest_framework.test import APITestCase

from locations.cities.tests import CITIES_URL
from locations.models import Location
from locations.streets.tests import STREET_URL

LOCATION_URL = '/locations/'


class LocationTests(APITestCase):

    def test_create_location(self):
        """
        Создание новой локации с id города и id улицы
        """
        response_city = self.client.post(CITIES_URL, {'title': 'Екатеринбург'}, format='json')
        response_street = self.client.post(STREET_URL,
                                           {
                                               'title': 'Ленина',
                                               'house': '1'
                                           },
                                           format='json')

        city_id = response_city.data.pop('id')
        street_id = response_street.data.pop('id')
        data = {
            'city':  city_id,
            'street': street_id
        }

        response = self.client.post(LOCATION_URL, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Location.objects.get().city.id, city_id)
        self.assertEqual(Location.objects.get().street.id, street_id)
