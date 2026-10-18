from django.contrib import admin

from account.models import Barber
from booking_manager.models import *

admin.site.register(Booking)
admin.site.register(BookingService)
admin.site.register(Product)
admin.site.register(Promotion)
admin.site.register(Barbershop)
admin.site.register(Comment)
