from django.contrib import admin
from .models import Samples


@admin.register(Samples)
class SamplesAdmin(admin.ModelAdmin):
    pass
