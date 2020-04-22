
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import MyUser, Profile


@receiver(post_save, sender=MyUser)
def user_created(sender, instance, created, **kwargs):
    if created:
        print(instance)
        Profile.objects.create(user=instance)



