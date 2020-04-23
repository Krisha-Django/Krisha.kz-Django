from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser, Profile


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff','role')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
    )

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'card_number', 'city')


