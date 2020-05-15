from django.db import models

from entries.models import Entry
from utils.models import BaseModel


class CarEntry(BaseModel):
    entry = models.OneToOneField(Entry, on_delete=models.CASCADE, primary_key=True)

