from django.contrib import admin
from .models import Reservation


# Register your models here.

@admin.register(Reservation)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'guest_id', 'room')
    search_fields = ['quest_id']
