from django.contrib import admin
from .models import Room


# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'type', 'status', 'price')
    search_fields = ['type', 'status', 'price']
