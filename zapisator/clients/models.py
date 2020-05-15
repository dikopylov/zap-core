from django.db import models

from utils.models import BaseModel
from zapisator import settings


class Client(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, primary_key=True)
