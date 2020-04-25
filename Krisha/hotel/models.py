from django.db import models
from city.models import City
from .validators import validate_name, validated_contact,validated_image


# Create your models here.
class HotelStarsManager(models.Manager):
    def one_starred_hotels(self):
        return super(HotelStarsManager, self).get_queryset().filter(type_by_star=1)

    def two_starred_hotels(self):
        return super(HotelStarsManager, self).get_queryset().filter(type_by_star=2)

    def three_starred_hotels(self):
        return super(HotelStarsManager, self).get_queryset().filter(type_by_star=3)

    def four_starred_hotels(self):
        return super(HotelStarsManager, self).get_queryset().filter(type_by_star=4)

    def five_starred_hotels(self):
        return super(HotelStarsManager, self).get_queryset().filter(type_by_star=5)


class HotelManager(models.Manager):
    pass


class Hotel(models.Model):
    TYPE_BY_STAR = (
        (1, "One Star"),
        (2, "Two-star"),
        (3, "Three-star"),
        (4, "Four-star"),
        (5, "Five-start")
    )

    name = models.CharField(max_length=100, validators=[validate_name],unique=True)
    description = models.CharField(max_length=255)
    type_by_star = models.IntegerField(choices=TYPE_BY_STAR, default=3)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hotels', null=True, blank=True)
    address = models.CharField(max_length=255, default=city.name)
    image = models.ImageField(upload_to='hotel_images', null=True, blank=True, validators=[validated_image])
    contact = models.CharField(max_length=12, validators=[validated_contact], unique=True)

    objects = HotelManager()
    by_stars_objects = HotelStarsManager()

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hotels"

    def __str__(self):
        return self.name

    @property
    def get_basic_information(self):
        return f'Name: {self.name}. Star: {self.type_by_star}. Description: {self.description}'
