import random

from booking_manager.models.booking_service import BookingService
from booking_manager.constants import CategoryChoices

from .utils import fake

def generate_services():

    services_count = BookingService.objects.count()
    services_to_create = max(0, 20 - services_count)

    service_names = [
        'Мужская стрижка',
        'Стрижка бороды',
        'Стрижка усов',
        'Массаж головы',
        'Модельная стрижка',
        'Оформление бороды',
        'Комплексная стрижка',
    ]

    booking_services = []

    for _ in range(services_to_create):
        booking_service = BookingService(
            name=random.choice(service_names),
            category=random.choice(list(CategoryChoices)),
            description=fake.text(),
            price=random.randint(10, 100),
        )

        booking_services.append(booking_service)

    BookingService.objects.bulk_create(booking_services)

    return booking_services