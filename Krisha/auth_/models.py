from django.db import models
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import PermissionsMixin, UserManager
from .validators import validate_birthday


#
from city.models import City


class MyAbstractUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, null=False, unique=True)
    first_name = models.CharField(max_length=255, null=False, default='')
    last_name = models.CharField(max_length=255, null=False, default='')
    email = models.EmailField(blank=True)
    birthday = models.DateField(null=True, validators=[validate_birthday])
    mobile = models.CharField(max_length=12, null=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        abstract = True
        # unique_together = ('first_name', 'last_name')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.first_name


class MyUser(MyAbstractUser):
    USER_ROLES = (
        (1, 'Admin'),
        (2, 'Customer'),
    )
    role = models.IntegerField(choices=USER_ROLES, default=2)


class ProfileManager(models.Manager):
    pass


class Profile(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='profiles',null=True,blank=True)
    card_number = models.CharField(max_length=16, null=True, blank=True)
    objects = ProfileManager()

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return f'Name: {self.user.first_name}. Email: {self.user.email}'
