from django.contrib import admin

from core.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass