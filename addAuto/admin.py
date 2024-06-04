from django.contrib import admin
from .models import addAuto
# Register your models here.
@admin.register(addAuto)
class addAutoAdmin(admin.ModelAdmin):
    list_display = ['price', 'name', 'count', 'year', 'image']