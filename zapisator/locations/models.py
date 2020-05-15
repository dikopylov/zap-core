from django.db import models

from locations.cities.models import City
from locations.streets.models import Street
from utils.models import BaseModel


class Location(BaseModel):
    city = models.ForeignKey(to=City, on_delete=models.DO_NOTHING)
    street = models.ForeignKey(to=Street, on_delete=models.DO_NOTHING)
