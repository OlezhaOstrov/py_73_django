from django.db import models
from booking_manager.models.base import BaseModel
from django.conf import settings
from booking_manager.models.barbershop import Barbershop
from booking_manager.models.raitingmixin import RatingMixin

class Barber(BaseModel, RatingMixin):
    experience = models.IntegerField()
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='barber',
    )
    name = models.CharField(max_length=50)
    barbershop = models.ForeignKey(Barbershop,
                                   on_delete=models.CASCADE,
                                   related_name='barber'
                                  )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'barbers'
        verbose_name = 'Барберы'
        verbose_name_plural = 'Барберы'
        ordering = ['-created_at','-experience']