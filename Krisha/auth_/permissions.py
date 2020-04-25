from rest_framework import permissions
from auth_.models import Profile, MyUser

SAFE_METHODS = ['GET', ]
class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in SAFE_METHODS:
                return True
            return request.user.role == 1
        return False


# class IsCustomer(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return request.user and request.user.is_authenticated
#
#     def has_object_permission(self, request, view, obj):
#         return Profile.objects.get(user=request.user).user.role == 2