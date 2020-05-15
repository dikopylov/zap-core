from django.db import models

from suppliers.executors.models import Executor
from utils.models import BaseModel


class HumanExecutor(BaseModel):
    executor = models.OneToOneField(Executor, on_delete=models.CASCADE, primary_key=True)
