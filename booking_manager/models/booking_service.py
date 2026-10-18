from django.core.validators import MinValueValidator
from django.db import models
from booking_manager.constants import CategoryChoices
from booking_manager.models.base import BaseModel

class BookingService(BaseModel):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100,
                                default=CategoryChoices.HAIRCUT,
                                choices=CategoryChoices,
                                verbose_name='Категория'
                                )
    description = models.TextField(blank=True,null=True)
    price = models.FloatField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'booking_services'
        ordering = ['-created_at','price']
        verbose_name = 'услуга'

