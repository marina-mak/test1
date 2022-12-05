from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Samples


@admin.register(Samples)
class SamplesAdmin(admin.ModelAdmin):
    list_display = ('sample_name', 'get_html_xrr')

    def get_html_xrr(self, object):
        if object.fig_xrr:
            return mark_safe(f"<img src='{object.fig_xrr.url}' width=100")
