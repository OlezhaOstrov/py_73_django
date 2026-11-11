import random

from booking_manager.models.booking import Booking
from account.models.client import Client
from account.models.barber import Barber
from booking_manager.models.booking_service import BookingService
from datetime import time

def generate_bookings():

    bookings_count = Booking.objects.count()
    bookings_to_create = max(0, 500 - bookings_count)

    clients_list = list(Client.objects.all())
    barbers_list = list(Barber.objects.all())
    services_list = list(BookingService.objects.all())

    visit_times = [
        time(11, 0),
        time(13, 30),
        time(14, 45),
        time(9, 15),
        time(17, 0),
        time(19, 0),
        time(15, 30),
    ]

    bookings = []

    for _ in range(bookings_to_create):
        booking = Booking(
            name='Бронирование',
            price=random.randint(10, 100),
            visit_time=random.choice(visit_times),
            is_active=True,
            booking_service=random.choice(services_list),
            client=random.choice(clients_list),
            barber=random.choice(barbers_list),
        )

        bookings.append(booking)

    Booking.objects.bulk_create(bookings)

    return bookings