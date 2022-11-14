from django.db import models
from uuid import uuid4


class BaseUuid(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid4(), editable=False)

# Create your models here.
class Samples(BaseUuid):
    sample_name = models.CharField("Название образца", max_length=100)
