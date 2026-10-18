from django.db import models
from booking_manager.models.base import BaseModel
from django.conf import settings
from booking_manager.models.barbershop import Barbershop

class Barber(BaseModel):
    experience = models.IntegerField()
    rating = models.IntegerField()
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
        verbose_name = 'Барбер'
        ordering = ['-created_at','-experience']