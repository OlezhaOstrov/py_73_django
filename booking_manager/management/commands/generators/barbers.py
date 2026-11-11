import random

from account.models.barber import Barber

from .utils import fake

def generate_barbers(users, barbershops):
    barbers_count = Barber.objects.count()
    barbers_to_create = max(0, 15 - barbers_count)

    barbers = []

    for i in range(barbers_to_create):
        barber = Barber(
            user=users[i],
            experience=random.randint(1, 15),
            name=fake.name(),
            barbershop=random.choice(barbershops),
            rating=random.randint(1, 5),
        )

        barbers.append(barber)

    Barber.objects.bulk_create(barbers)

    return barbers
