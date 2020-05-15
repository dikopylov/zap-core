from rest_framework import status
from rest_framework.test import APITestCase

from locations.streets.models import Street

STREET_URL = '/streets/'


class StreetTests(APITestCase):
    def test_create_street(self):
        """
        Создание улицы
        """
        data = {'title': 'Ленина', 'house': '12/1'}
        response = self.client.post(STREET_URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Street.objects.get().title, 'Ленина')
        self.assertEqual(Street.objects.get().house, '12/1')