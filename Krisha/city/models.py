from django.db import models


# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name


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
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    type_by_size = models.CharField(choices=TYPE_BY_SIZE, default="M")
    type_by_location = models.IntegerField(choices=TYPE_BY_LOCATION, default=1)
    type_by_target = models.IntegerField(choices=TYPE_BY_TARGET, default=1)
    type_by_star = models.IntegerField(choices=TYPE_BY_STAR, default=3)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hotels')
    address = models.CharField(max_length=255, default=city.name)
    image = models.ImageField(upload_to='hotel_images', null=True, blank=True)
    contact = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hotels"

    def __str__(self):
        return self.name

    @property
    def get_basic_information(self):
        return f'Name: {self.name}. Star: {self.type_by_star}. Description: {self.description}'
