from django.db import models
from booking_manager.models.base import BaseModel
from booking_manager.models.booking_service import BookingService
from account.models.client import Client
from account.models.barber import Barber
from booking_manager.managers import BookingManager


class Booking(BaseModel):
    name = models.CharField(max_length=100,
                            verbose_name='Название',
                            )
    price = models.FloatField(verbose_name='Цена',
                              null=True,
                              blank=True)

    visit_time = models.TimeField(null=True,blank=True,verbose_name='Время визита')
    is_active = models.BooleanField(default=True,verbose_name='Активно')

    booking_service = models.ForeignKey(BookingService,
                                        related_name='bookings',
                                        on_delete=models.SET_NULL,
                                        verbose_name='услуги',
                                        null=True)
    client = models.ForeignKey(Client,related_name='bookings',on_delete=models.SET_NULL,null=True)
    barber = models.ForeignKey(Barber,related_name='bookings',on_delete=models.SET_NULL,null=True)


    def __str__(self):
        return self.name

    objects = BookingManager()

    class Meta:
        db_table = 'booking'
        ordering = ['-created_at']
        verbose_name = 'Бронирования'
        verbose_name_plural = 'Бронирования'

