from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from clients.models import Client
from entries.models import Entry
from locations.cities.models import City
from locations.models import Location
from locations.streets.models import Street
from services.car_service.models import CarService
from services.models import Service
from suppliers.companies.models import Company
from suppliers.executors.human_executors.models import HumanExecutor
from suppliers.executors.models import Executor

CAR_ENTRIES_URL = '/api/car-entries/'


class CarEntryTests(APITestCase):

    def test_create_car_entry(self):
        """
        Создание записи автоуслуги
        """

        city = City.objects.create(title='Екатеринбург')
        street = Street.objects.create(title='Розы', house='12/1')
        location = Location.objects.create(city=city, street=street)

        company_data = {
            'title': 'Шиномонтаж №1',
            'description': 'Самый лучший',
        }

        company = Company.objects.create(**company_data)
        company.locations.add(location)
        company.save()

        service_data = {
                'title': 'Мойка',
                'description': 'Экспресс',
                'price': 999.99,
                'duration': "20:00",
                'company': company
        }

        user_data = {
            'email': 'test@test.com',
            'phone': '89123456789',
            'password': '1234567890'
        }

        user = get_user_model().objects.create(**user_data)

        service = Service.objects.create(**service_data)
        car_service = CarService.objects.create(service=service)
        client = Client.objects.create(user=user)
        executor = Executor.objects.create(title='Иван')
        executor.save()
        executor.services.add(service)
        human_executor = HumanExecutor.objects.create(executor=executor)

        entry_data = {
            'entry': {
                'status': Entry.Statuses.NEW,
                'service': car_service.service_id,
                'client': client.user_id,
                'executor': human_executor.executor_id,
                'entry_at': '2020-02-02 15:00:00'
            },
        }

        response = self.client.post(CAR_ENTRIES_URL, entry_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
