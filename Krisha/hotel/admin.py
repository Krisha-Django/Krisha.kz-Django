from django.contrib import admin
from .models import Hotel


# Register your models here.
@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'type_by_star', 'city')
    search_fields = ['name', 'type_by_star', 'city']

