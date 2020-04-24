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


class HotelTargetManager(models.Manager):
    def airport_hotels(self):
        return super(HotelTargetManager, self).get_queryset().filter(type_by_target=1)

    def business_hotels(self):
        return super(HotelTargetManager, self).get_queryset().filter(type_by_target=2)

    def bed_and_breakfast_hotels(self):
        return super(HotelTargetManager, self).get_queryset().filter(type_by_target=3)

    def casino_hotels(self):
        return super(HotelTargetManager, self).get_queryset().filter(type_by_target=4)

    def resorts_hotels(self):
        return super(HotelTargetManager, self).get_queryset().filter(type_by_target=5)

    def self_catering_hotels(self):
        return super(HotelTargetManager, self).get_queryset().filter(type_by_target=6)

    def service_apartments(self):
        return super(HotelTargetManager, self).get_queryset().filter(type_by_target=7)

    def suite_hotels(self):
        return super(HotelTargetManager, self).get_queryset().filter(type_by_target=8)


class HotelLocationManager(models.Manager):
    def airport_hotels(self):
        return super(HotelLocationManager, self).get_queryset().filter(type_by_location=1)

    def boatels(self):
        return super(HotelLocationManager, self).get_queryset().filter(type_by_lcoation=2)

    def city_center(self):
        return super(HotelLocationManager, self).get_queryset().filter(type_by_location=3)

    def motel(self):
        return super(HotelLocationManager, self).get_queryset().filter(type_by_location=4)

    def surub_hotels(self):
        return super(HotelLocationManager, self).get_queryset().filter(type_by_location=5)

    def floating_hotels(self):
        return super(HotelLocationManager, self).get_queryset().filter(type_by_location=6)

    def resorts(self):
        return super(HotelLocationManager, self).get_queryset().filter(type_by_location=7)

    def rotels(self):
        return super(HotelLocationManager, self).get_queryset().filter(type_by_location=8)

    def self_catering_hotels(self):
        return super(HotelLocationManager, self).get_queryset().filter(type_by_location=9)


class HotelSizeManager(models.Manager):
    def very_small_hotels(self):
        return super(HotelSizeManager, self).get_queryset().filter(type_by_size=1)

    def small_hotels(self):
        return super(HotelSizeManager, self).get_queryset().filter(type_by_size=2)

    def medium_hotels(self):
        return super(HotelSizeManager, self).get_queryset().filter(type_by_size=3)

    def large_hotels(self):
        return super(HotelSizeManager, self).get_queryset().filter(type_by_size=4)

    def mega_hotels(self):
        return super(HotelSizeManager, self).get_queryset().filter(type_by_size=5)


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
    TYPE_BY_TARGET = (
        (1, "Airport Hotel"),
        (2, 'Business Hotel'),
        (3, "Bed and Breakfast Hotel"),
        (4, "Casino Hotels"),
        (5, "Resorts"),
        (6, "Self-Catering Hotels"),
        (7, "Service Apartments"),
        (8, "Suite Hotels")
    )
    TYPE_BY_LOCATION = (
        (1, "Airport Hotel"),
        (2, "Boatels"),
        (3, "City Center"),
        (4, "Motel"),
        (5, "Suburb Hotels"),
        (6, "Floating Hotels"),
        (7, "Resorts"),
        (8, "Rotels"),
        (9, "Self-Catering Hotels")
    )
    TYPE_BY_SIZE = (
        ("VS", "Very Small"),
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
        ("MG", "MEGA")
    )
    name = models.CharField(max_length=100, validators=[validate_name])
    description = models.CharField(max_length=255)
    type_by_size = models.CharField(max_length=2, choices=TYPE_BY_SIZE, default="M")
    type_by_location = models.IntegerField(choices=TYPE_BY_LOCATION, default=1)
    type_by_target = models.IntegerField(choices=TYPE_BY_TARGET, default=1)
    type_by_star = models.IntegerField(choices=TYPE_BY_STAR, default=3)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hotels', null=True, blank=True)
    address = models.CharField(max_length=255, default=city.name)
    image = models.ImageField(upload_to='hotel_images', null=True, blank=True,validators=[validated_image])
    contact = models.CharField(max_length=12, validators=[validated_contact])

    objects = HotelManager()
    by_stars_objects = HotelStarsManager()
    by_target_objects = HotelTargetManager()
    by_location_objects = HotelLocationManager()
    by_size_objects = HotelSizeManager()

    # Queries on default custom model manager
    # Hotel.objects.all()
    # Hotel.objects.one_starred()
    # Hotel.objects.two starred()

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hotels"

    def __str__(self):
        return self.name

    @property
    def get_basic_information(self):
        return f'Name: {self.name}. Star: {self.type_by_star}. Description: {self.description}'
    #
    # @property
    # def likes_count(self):
    #     return Like.objects.filter(Hotel=self).count()
