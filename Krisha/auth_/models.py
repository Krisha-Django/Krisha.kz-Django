from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import PermissionsMixin, UserManager


class MyUserManager(UserManager):
    pass

#
class MyAbstractUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, null=False, unique=True)
    first_name = models.CharField(max_length=255, null=False, default='')
    second_name = models.CharField(max_length=255, null=False, default='')
    email = models.EmailField(blank=True)
    birthday = models.DateField(null=True)
    mobile = models.CharField(max_length=12, null=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = MyUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        abstract = True


class MyUser(MyAbstractUser):
    card_number = models.CharField(max_length=16, default=0)

    class Meta:
        verbose_name = 'my_user'
        verbose_name_plural = 'my_users'


class ProfileManager(models.Manager):
    pass


class Profile(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    objects = ProfileManager()

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return f'Name: {self.user.first_name}. Email: {self.user.email}'
