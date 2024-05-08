from django.contrib import admin

from apps.vendor.models import HistoricalPerformance, Vendor

# Register your models here.

admin.site.register(Vendor)
admin.site.register(HistoricalPerformance)
