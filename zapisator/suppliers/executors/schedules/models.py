from django.db import models

from suppliers.executors.models import Executor
from suppliers.suppliers_employees.models import SupplierEmployee
from utils.models import BaseModel


class Schedule(BaseModel):
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    executor = models.ForeignKey(Executor, related_name='schedules', on_delete=models.CASCADE)


class LunchBreak(BaseModel):
    started_at = models.TimeField()
    ended_at = models.TimeField()
    schedule = models.ForeignKey(Schedule, related_name='lunch_breaks', on_delete=models.CASCADE)
