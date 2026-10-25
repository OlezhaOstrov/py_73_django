from booking_manager.models.base import BaseModel
from django.db import models

class ProductBooking(BaseModel):
    product = models.ForeignKey(to='Product',
                                on_delete=models.CASCADE,
                                related_name='booking_items',)
    booking = models.ForeignKey(to='Booking',
                                on_delete=models.CASCADE,
                                related_name='product_items',)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.product.name

    class Meta:
        db_table = 'product_booking'
        ordering = ['-created_at']
        verbose_name = 'Товары и бронирования'
        verbose_name_plural = 'Товары и бронирования'