from django.db import models
from django.db.models.fields import PositiveSmallIntegerField
from booking_manager.models.booking_service import BookingService

from booking_manager.models.base import BaseModel
class Promotion(BaseModel):
    name = models.CharField(max_length=100,verbose_name='Название акции')
    description = models.TextField(verbose_name='Описание акции')
    discount_percent = PositiveSmallIntegerField(verbose_name='Размер скидки в процентах')
    start_date = models.DateTimeField(verbose_name='Дата начала акции')
    end_time = models.DateTimeField(verbose_name='Дата окончания акции')
    services = models.ManyToManyField(BookingService, related_name='promotions')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'promotions'
        ordering = ['-created_at']