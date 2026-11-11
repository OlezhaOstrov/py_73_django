import random
from datetime import timedelta

from django.utils import timezone

from booking_manager.models.promotion import Promotion
from booking_manager.models.booking_service import BookingService

from .utils import fake

def generate_promotions():

    promotions_count = Promotion.objects.count()
    promotions_to_create = max(0, 10 - promotions_count)

    promotions = []

    for _ in range(promotions_to_create):
        start = timezone.now()

        promotions.append(
            Promotion(
                name='Скидка на стрижку',
                description=fake.text(),
                discount_percent=random.randint(10, 80),
                start_date=start,
                end_time=start + timedelta(days=30),
            )
        )

    Promotion.objects.bulk_create(promotions)

    services = list(BookingService.objects.all())

    new_promotions = list(
        Promotion.objects.order_by('-id')[:promotions_to_create]
    )

    for promotion in new_promotions:
        promotion.services.add(random.choice(services))

    return new_promotions