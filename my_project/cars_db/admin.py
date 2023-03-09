from django.contrib import admin
from .models import Car

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('year', 'make', 'model', 'color')
    search_fields = ['year', 'make', 'model']
    list_filter = ('year', 'make', 'model', 'color')

admin.site.register(Car, CarAdmin)
