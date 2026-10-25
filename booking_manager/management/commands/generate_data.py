import random
from datetime import time, timedelta

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker

from booking_manager.models.barbershop import Barbershop
from account.models.barber import Barber
from account.models.client import Client
from booking_manager.models.booking_service import BookingService
from booking_manager.models.products import Product
from booking_manager.models.booking import Booking
from booking_manager.models.promotion import Promotion
from booking_manager.models.productbooking import ProductBooking
from booking_manager.models.comment import Comment
from booking_manager.constants import CategoryChoices


fake = Faker('ru_RU')

class Command(BaseCommand):

    help = 'Генерация тестовых данных для Booking Manager'

    def handle(self, *args, **options):

        # 1. Получаем свободных пользователей

        users = list(
            User.objects
            .filter(barber__isnull=True, client__isnull=True)
            .order_by('id')
        )

        barbers_count = Barber.objects.count()
        clients_count = Client.objects.count()
        barbers_to_create = max(0, 15 - barbers_count)
        clients_to_create = max(0, 80 - clients_count)

        required_users = barbers_to_create + clients_to_create

        if len(users) < required_users:
            self.stdout.write(
                self.style.ERROR(
                    f'Недостаточно свободных пользователей: {len(users)}. '
                    f'Нужно: {required_users}.'
                )
            )
            return

        # 2. Создаём недостающие филиалы
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
        barbershops = list(Barbershop.objects.all())


        # 3. Создаём недостающих барберов

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


        # 4. Создаём недостающих клиентов

        client_statuses = ['new', 'regular', 'vip']
        clients = []
        for i in range(clients_to_create):
            client = Client(
                user=users[barbers_to_create + i],
                name=fake.name(),
                phone=fake.unique.numerify(text='###########'),
                status=random.choice(client_statuses),
            )
            clients.append(client)
        Client.objects.bulk_create(clients)


        # 5. Создаём недостающие услуги

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


        # 6. Создаём недостающие товары

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


        # 7. Создаём недостающие бронирования

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


        # 8. Создаём недостающие комментарии

        comments_count = Comment.objects.count()
        comments_to_create = max(0, 200 - comments_count)
        bookings_without_comments = list(
            Booking.objects.filter(comment__isnull=True)
        )
        comments = []
        for booking in bookings_without_comments[:comments_to_create]:
            comments.append(
                Comment(
                    text=fake.text(),
                    is_published=True,
                    client=booking.client,
                    barber=booking.barber,
                    booking=booking,
                    rating=random.randint(1, 5),
                )
            )
        Comment.objects.bulk_create(comments)


        # 9. Создаём недостающие акции

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


        # Связываем акции с услугами

        services = list(BookingService.objects.all())
        new_promotions = list(
            Promotion.objects.order_by('-id')[:promotions_to_create]
        )
        for promotion in new_promotions:
            promotion.services.add(random.choice(services))


        # 10. Добавляем товары в бронирования

        products = list(Product.objects.all())
        bookings_without_products = list(
            Booking.objects.filter(product_items__isnull=True)
        )
        product_booking_items = []
        for booking in random.sample(
            bookings_without_products,
            k=min(100, len(bookings_without_products)),
        ):
            product_booking_items.append(
                ProductBooking(
                    booking=booking,
                    product=random.choice(products),
                    quantity=1,
                )
            )
        ProductBooking.objects.bulk_create(product_booking_items)
        self.stdout.write(
            self.style.SUCCESS('Генерация данных завершена')
        )









