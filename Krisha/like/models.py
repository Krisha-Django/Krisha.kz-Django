from django.db import models

# Create your models here.
from django.db import models
from hotel.models import Hotel
from auth_.models import MyUser


# Create your models here.
class Like(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"