from django.db import models
from .validators import validate_name
# Create your models here.

class City(models.Model):

    name = models.CharField(max_length=50, validators=[validate_name],unique=True)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name
