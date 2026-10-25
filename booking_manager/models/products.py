from django.db import models
from booking_manager.models.base import BaseModel
from booking_manager.models.booking import Booking

class Product(BaseModel):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    bookings = models.ManyToManyField(Booking,
                                      related_name='products',
                                      through='ProductBooking',)

    class Meta:
        db_table = 'product'
        ordering = ['-created_at','price']
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

