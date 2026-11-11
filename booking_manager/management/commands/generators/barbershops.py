from datetime import time
from booking_manager.models.barbershop import Barbershop
from .utils import fake

def generate_barbershops():
    barbershops = list(Barbershop.objects.all())

    if len(barbershops) < 5:
        new_barbershops = []

        for _ in range(5 - len(barbershops)):
            barbershop = Barbershop(
                name=f'Филиал {fake.city()}',
                address=fake.address(),
                phone=fake.phone_number()[:100],
                description=fake.text(),
                opening_time=time(9, 0),
                closed_time=time(21, 0),
                is_active=True,
            )

            new_barbershops.append(barbershop)

        Barbershop.objects.bulk_create(new_barbershops)

    return list(Barbershop.objects.all())