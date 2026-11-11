from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from account.models.barber import Barber
from account.models.client import Client

from .generators.barbershops import generate_barbershops
from .generators.barbers import generate_barbers
from .generators.clients import generate_clients
from .generators.services import generate_services
from .generators.products import generate_products
from .generators.bookings import generate_bookings
from .generators.comments import generate_comments
from .generators.promotions import generate_promotions
from .generators.product_bookings import generate_product_bookings

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

        # 2. Создаём филиалы

        barbershops = generate_barbershops()

        # 3. Создаём барберов

        generate_barbers(
            users[:barbers_to_create],
            barbershops
        )

        # 4. Создаём клиентов

        generate_clients(
            users[barbers_to_create:required_users]
        )

        # 5. Создаём услуги

        generate_services()

        # 6. Создаём товары

        generate_products()

        # 7. Создаём бронирования

        generate_bookings()

        # 8. Создаём комментарии

        generate_comments()

        # 9. Создаём акции

        generate_promotions()

        # 10. Добавляем товары в бронирования

        generate_product_bookings()

        self.stdout.write(
            self.style.SUCCESS('Генерация данных завершена')
        )









