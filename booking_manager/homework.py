from booking_manager.models import Booking
from booking_manager.constants import CategoryChoices
from datetime import date

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


