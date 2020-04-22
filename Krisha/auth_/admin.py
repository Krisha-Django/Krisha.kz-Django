
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from auth_.models import MyUser, Profile


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
     list_display = ('username', 'email',)
     fieldsets = (
       (None, {'fields': ('username', 'password')}),
     )
# admin.register(MyUser)
admin.site.register(Profile)

