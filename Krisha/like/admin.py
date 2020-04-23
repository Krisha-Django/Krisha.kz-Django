from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Like
# Register your models here.
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'hotel', 'user')
    search_fields = ['hotel']