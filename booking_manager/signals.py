from django.db.models.signals import post_save, post_delete
from django.db.models import Avg
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db import transaction
from django.core.cache import cache

from account.models.client import Client
from booking_manager.models.comment import Comment
from booking_manager.models.booking import Booking
from booking_manager.constants import ClientChoices
from booking_manager.models.booking_service import BookingService


User = get_user_model()  # импортируем модель юзера которая сейчас работает


# задание 1
@receiver(post_save, sender=User)
def create_client(sender, instance, created, **kwargs):
    if created:
        client, client_created = Client.objects.get_or_create(
            user=instance)  # instance - конкретный обьект пользователя в данном случае(например создали рользователя Oleg - то Oleg будет instance)



# задание 2
def update_barber_rating(barber):
    barber_rating = Comment.objects.filter(
        is_published=True,
        barber=barber
    ).aggregate(average=Avg('rating'))['average']

    barber.rating = barber_rating
    barber.save(update_fields=['rating'])


@receiver(post_save, sender=Comment)
def comment_saved(sender, instance, **kwargs):
    if instance.barber:
        update_barber_rating(instance.barber)


@receiver(post_delete, sender=Comment)
def comment_deleted(sender, instance, **kwargs):
    if instance.barber:
        update_barber_rating(instance.barber)



# задание 3
def update_status_client(client):
    booking_client = Booking.objects.filter(
        client=client,
        is_active=False).count()

    if booking_client <= 2:
        client.status = ClientChoices.NEW
    elif booking_client >= 3 and booking_client <= 9:
        client.status = ClientChoices.REGULAR
    else:
        client.status = ClientChoices.VIP
    client.save(update_fields=['status'])


@receiver(post_save, sender=Booking)
def saved_status(sender, instance, **kwargs):
    update_status_client(instance.client)


@receiver(post_delete, sender=Booking)
def deleted_status(sender, instance, **kwargs):
    update_status_client(instance.client)



#DatabaseCache
@receiver(post_save, sender=BookingService)
@receiver(post_delete, sender=BookingService)
def invalidate_services_cache(sender, instance, **kwargs):
    transaction.on_commit(
        lambda: cache.delete('services_active')
    )


@receiver(post_save, sender=Client)
@receiver(post_delete,  sender=Client)
def client_saved(sender, instance, **kwargs):
    transaction.on_commit(
        lambda: cache.delete(f'client_profile_{instance.pk}')
    )





