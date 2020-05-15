from django.db import models

from clients.models import Client
from services.models import Service
from suppliers.executors.models import Executor
from suppliers.suppliers_employees.models import SupplierEmployee
from utils.models import BaseModel
from django.utils.translation import ugettext_lazy as _


class Entry(BaseModel):
    class Statuses(models.TextChoices):
        NEW = 'new', _('Новый')
        IN_PROGRESS = 'in_progress', _('В обработке')
        PROCESSED = 'processed', _('Обработан')

    status = models.CharField(
        max_length=20,
        choices=Statuses.choices,
        default=Statuses.NEW,
    )

    entry_at = models.DateTimeField()
    client = models.ForeignKey(Client, related_name='entries', on_delete=models.DO_NOTHING, blank=True, null=True)
    executor = models.ForeignKey(Executor, related_name='entries', on_delete=models.DO_NOTHING)
    service = models.ForeignKey(Service, related_name='entries', on_delete=models.DO_NOTHING)
