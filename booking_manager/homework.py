from booking_manager.models import Booking
from booking_manager.constants import CategoryChoices
from datetime import date
from django.db.models import Count, Min, Max, Avg, F, Sum,Q
from booking_manager.models.booking import BookingService
from account.models.barber import Barber
from account.models.client import Client
from functools import lru_cache


#Получить все задачи из базы данных.
qs = Booking.objects.all()

#Получить все бронирования, цена которых больше 100.
qs1 = Booking.objects.filter(price__gt = 100)

#Найти бронирования, в названии которых содержится строка "стрижка" без учёта регистра.
qs2 = Booking.objects.filter(name__icontains = 'стрижка')

# Получить бронирования, название которых начинается с "Муж", без учёта регистра.
qs3 = Booking.objects.filter(name__istartwith = 'Муж')

#Получить все бронирования, у которых не указано время визита.
qs4 = Booking.objects.filter(visit_time__isnull=True)

#Получить активные бронирования определённой категории, например HAIRCUT, цена которых не превышает 100
qs5 = Booking.objects.filter(is_active=True,
                             category=CategoryChoices.BEARD,
                             price__lte=100)

#Получить все бронирования, относящиеся к категориям HAIRCUT и MOUSTACHE
qs6 = Booking.objects.filter(category__in = [CategoryChoices.MUSTACHE,CategoryChoices.HAIRCUT])

#Получить все бронирования, кроме неактивных записей с ценой меньше 50.
qs7 = Booking.objects.filter(is_active = False,price__lt = 50)

#Найти все бронирования, созданные сегодня
qs8 = Booking.objects.filter(created_at__date = date.today())

#Увеличить или изменить цену всех бронирований определённой категории на фиксированное значение,
# например установить цену 120.
qs9 = Booking.objects.filter(category = CategoryChoices.HAIRCUT).update(price = 120)

#Сделать все бронирования с ценой выше 200 неактивными.
qs10 = Booking.objects.filter(price__gt = 200).update(is_active = False)

#Для всех бронирований, у которых visit_time не указан, установить is_active=False.
qs11 = Booking.objects.filter(visit_time__isnull=True).update(is_active = False)

# Удалить все неактивные бронирования, цена которых меньше 20.
qs12 = Booking.objects.filter(price__lt = 20).delete()



#АГГРЕГАЦИЯ и АННОТАЦИЯ
#задание 1
services = BookingService.objects.aggregate(
  count_services = Count('id'),
  min_price = Min('price'),
  max_price = Max('price'),
  avg_price = Avg('price')
)


#задание 2
barbers = Barber.objects.annotate(
    count_bookings = Count('bookings')).order_by('-count_bookings')
for barber in barbers:
  print(barber.name, barber.count_bookings)


#задание 3
services = BookingService.objects.annotate(
    count_services = Count('bookings')).filter(count_services__gt = 3)


#задание 4
clients = Client.objects.annotate(count_bookings = Count('bookings'))
average = clients.aggregate(avg_bookings = Avg('count_bookings'))
result = clients.filter__gt = average['(avg_bookings']


#задание 5
barbers = Barber.objects.annotate(
    avg_rating = Avg('comment__rating')).filter(avg_rating__gt = 4.5)


#задание 6
quantity_bookings = Barber.objects.annotate(
  count_is_active_bookings = Count('bookings', filter = Q(bookings__is_active = True)),
  count_is_not_active_bookings = Count('bookings',filter = Q(bookings__is_active = False))
)


#задание 7
clients = Client.objects.annotate(
    total_spent = Sum('bookings__booking_service__price')).filter(total_spent__gt = 1000)


#задание 8
client_bookings = Booking.objects.annotate(
    products_total = Sum(F('product_items__quantity')* F('product_items__product__price')))





#Рекурсия с кэшированием
@lru_cache(maxsize=123)
def sum_numbers(numbers):
    if not numbers:
        return 0
    if numbers[0] > 0:
        return numbers[0] + sum_numbers(numbers[1:])
print(sum_numbers((2,4,-5,-1,7,-4)))
