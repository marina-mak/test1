from django.db import models
from uuid import uuid4


class BaseUuid(models.Model):
   id = models.UUIDField(primary_key=True, default=uuid4(), editable=False)


# Create your models here.
class Samples(BaseUuid):
   sample_name = models.CharField("Название образца", max_length=100)
   formula = models.CharField(blank=True, null=True, max_length=50)
   fabrication = models.TextField(blank=True)
   fig_xrr = models.ImageField(upload_to="XRR_data/", default='XRR_data/')
   fig_xrd = models.ImageField(upload_to="XRD_data/", default='XRD_data/')
