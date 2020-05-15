from django.db import models

from utils.models import BaseModel


class City(BaseModel):
    title = models.CharField(max_length=255)
