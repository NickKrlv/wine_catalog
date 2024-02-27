from django.contrib import admin
from . import models


@admin.register(models.Wine)
class WineAdmin(admin.ModelAdmin):
    list_display = ('name', 'grape_variety', 'is_active')
    list_editable = ('is_active',)
    prepopulated_fields = {'slug': ('name',)}
