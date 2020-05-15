from django.db import models

from utils.models import BaseModel


class Supplier(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)