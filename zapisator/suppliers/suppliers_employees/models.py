from django.db import models

from suppliers.companies.models import Company
from utils.models import BaseModel
from zapisator import settings


class SupplierEmployee(BaseModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, primary_key=True)
    company = models.ForeignKey(Company, related_name='supplier_employees', on_delete=models.CASCADE)