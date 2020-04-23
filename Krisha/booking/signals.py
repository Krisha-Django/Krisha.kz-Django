
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Reservation
from room.models import Room


@receiver(post_save, sender=Reservation)
def reservation_created(sender, instance, update_fields, **kwargs):
    if update_fields:
        room = instance.room
        status = False
        if room.status:
            status = False
        else:
            status = True
        Room.objects.filter(id=room.id).update(status=status)

@receiver(post_save, sender=Reservation)
def reservation_terminated(sender, instance, **kwargs):
    if instance.terminate:
        terminated = instance.terminate
        room = instance.room
        status = True
        if terminated:
            status = False
        Room.objects.filter(id=room.id).update(status = status)





    # @receiver([post_save, post_delete, post_update], sender=PointAward)
    # def on_point_award_changed(sender, **kwargs):
    #     instance = kwargs.get('instance')
    #     if instance:
    #         key = 'acct-{0}-points'.format(instance.id)
    #         cache.delete(key)





