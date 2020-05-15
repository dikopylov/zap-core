from django.db import models

from locations.cities.models import City
from utils.models import BaseModel


class Street(BaseModel):
    title = models.CharField(max_length=255)
    house = models.CharField(max_length=10)
