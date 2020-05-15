from django.db import models

from suppliers.companies.models import Company
from utils.models import BaseModel


class Service(BaseModel):
    """
        Базовый класс для всех услуг. Является отдельной таблице
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    duration = models.DurationField()

    company = models.ForeignKey(to=Company, on_delete=models.CASCADE)