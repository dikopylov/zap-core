from rest_framework import status
from rest_framework.test import APITestCase

from locations.cities.models import City
from locations.models import Location
from locations.streets.models import Street

COMPANY_URL = '/companies/'


class CompanyTests(APITestCase):

    def test_create_company(self):
        """
        Создание компании с id локации
        """

        city = City.objects.create(title='Екатеринбург')
        street = Street.objects.create(title='Ленина', house='28а')
        location = Location.objects.create(city=city, street=street)

        data = {
            'title': 'Автокомплекс #1',
            'description': 'Топ мойки',
            'locations': [location.id]
        }

        response = self.client.post(COMPANY_URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_companies(self):
        """
        Получение всех компании
        """

        city = City.objects.create(title='Екатеринбург')
        street = Street.objects.create(title='Ленина', house='28а')
        location = Location.objects.create(city=city, street=street)

        data = {
            'title': 'Автокомплекс #1',
            'description': 'Топ мойки',
            'locations': [location.id]
        }

        for counter in range(1, 22):
            self.client.post(COMPANY_URL, data, format='json')

        response = self.client.get(COMPANY_URL, data, format='json')
        links = response.data.pop('links')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.pop('count'), 21)
        self.assertIsNotNone(links)
        self.assertTrue('first' in links)
        self.assertTrue('previous' in links)
        self.assertTrue('current' in links)
        self.assertTrue('next' in links)
        self.assertTrue('last' in links)
