import datetime
import uuid

from django.db import models

from utils.models import BaseModel
from zapisator import settings


def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    now = datetime.datetime.now()
    return 'media/users/{0}/{1}/{2}/{3}'.format(now.year,
                                                now.month,
                                                now.day,
                                                filename)


class UserFile(BaseModel):
    file = models.FileField(upload_to=user_directory_path)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='files', on_delete=models.DO_NOTHING)
