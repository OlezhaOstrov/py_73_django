from django.core.cache import cache
from booking_manager.models.booking_service import BookingService
from account.models.client import Client
from booking_manager.constants import ClientChoices

#задание 2 Database кэш
def get_active_services():
    services = cache.get('services_active')
    if services is None:
        services = list(BookingService.objects.filter(
            is_active = True,
        )
    )
        cache.set('services_active', services,600)
    return services


def get_client_profile(client_id):
    cache_key = f'client_profile_{client_id}'
    client_profile = cache.get(cache_key)
    if client_profile is None:
        client = Client.objects.get(id=client_id)
        client_profile = {
            'name': client.name,
            'status':client.status,
            'bookings_count': client.bookings.count()
        }
        cache.set(f'client_profile_{client_id}', client_profile,900)
    return client_profile



