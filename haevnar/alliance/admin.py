from django.contrib import admin

from .models import Group

# Register your models here.
@admin.register(Group)
class CorporationAdmin(admin.ModelAdmin):
    list_display = ["name", "approved"]