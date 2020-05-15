from django.db import models

from services.models import Service
from utils.models import BaseModel


class CarService(BaseModel):
    service = models.OneToOneField(Service, on_delete=models.CASCADE, primary_key=True)
