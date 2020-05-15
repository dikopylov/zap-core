from django.db import models

from services.models import Service
from utils.models import BaseModel


class Executor(BaseModel):
    title = models.CharField(max_length=255)
    services = models.ManyToManyField(Service, related_name='executors')
