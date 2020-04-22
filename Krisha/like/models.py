from django.db import models
from hotel.models import Hotel


# Create your models here.
class Like(models.Model):
    # user = models.FK(related_names = 'likes', on_delete=cascade
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'
