from django.db import models

from locations.models import Location
from suppliers.models import Supplier
from utils.models import BaseModel


class Company(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['-id']
