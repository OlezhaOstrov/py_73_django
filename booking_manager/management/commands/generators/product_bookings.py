import random

from booking_manager.models.products import Product
from booking_manager.models.booking import Booking
from booking_manager.models.productbooking import ProductBooking

def generate_product_bookings():

    products = list(Product.objects.all())

    bookings_without_products = list(
        Booking.objects.filter(product_items__isnull=True)
    )

    product_booking_items = []

    selected_bookings = random.sample(
        bookings_without_products,
        k=min(100, len(bookings_without_products)),
    )

    for booking in selected_bookings:
        product_booking_items.append(
            ProductBooking(
                booking=booking,
                product=random.choice(products),
                quantity=1,
            )
        )

    ProductBooking.objects.bulk_create(product_booking_items)

    return product_booking_items