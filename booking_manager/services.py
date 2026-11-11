from booking_manager.models.productbooking import  ProductBooking
from booking_manager.models.booking import Booking
from django.db import transaction
from booking_manager.models.products import Product
from booking_manager.models.booking_service import BookingService
from account.models.barber import Barber
from account.models.client import Client


# задание 4
booking_service = BookingService.objects.get(id=1)
client = Client.objects.get(id=1)
barber = Barber.objects.get(id=1)
product1 = Product.objects.get(id=1)
product2 = Product.objects.get(id=4)
products_booking = [
    (product1, 2),
    (product2, 1)
]
def created_booking_with_products(barber, client, booking_service, products_booking):
    with transaction.atomic():
        booking = Booking.objects.create(
            name='Booking_1',
            price=35,
            booking_service=booking_service,
            client=client,
            barber=barber
        )

        for product, quantity in products_booking:
            if quantity > product.stock_quantity:
                raise ValueError('недостаточно товара на складе')
            ProductBooking.objects.create(
                product=product,
                booking=booking,
                quantity=quantity
            )
            product.stock_quantity -= quantity
            product.save(update_fields=['stock_quantity'])




# задание 6
def created_bookings(name,barber, client, visit_time,booking_service,price):
    with transaction.atomic():
        locked_barber = Barber.objects.select_for_update().get(id=barber.id)

        if Booking.objects.filter(
            barber=locked_barber,
            is_active=True,
            visit_time=visit_time
        ).exists():
            raise ValueError ('Барбер уже занят на это время')

        return Booking.objects.create(
            name=name,
            price=booking_service.price,
            booking_service=booking_service,
            client=client,
            barber=locked_barber
        )

