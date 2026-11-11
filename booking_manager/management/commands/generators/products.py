import random

from booking_manager.models.products import Product

from .utils import fake

def generate_products():

    products_count = Product.objects.count()
    products_to_create = max(0, 50 - products_count)

    products = []

    for _ in range(products_to_create):
        product = Product(
            name=fake.word().capitalize(),
            price=random.randint(10, 40),
            description=fake.text(),
        )

        products.append(product)

    Product.objects.bulk_create(products)

    return products