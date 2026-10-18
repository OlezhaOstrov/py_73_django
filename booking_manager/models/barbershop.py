from django.db import models
from booking_manager.models.base import BaseModel
class Barbershop(BaseModel):
    name = models.CharField(max_length=50,verbose_name='Название филиала')
    address = models.CharField(max_length=150,verbose_name='Адрес')
    phone = models.CharField(max_length=100,verbose_name='Контактный телефон')
    description = models.TextField(null=True,blank=True,verbose_name='Описание')
    opening_time = models.TimeField(verbose_name='Время открытия')
    closed_time = models.TimeField(verbose_name='Время закрытия')
    is_active = models.BooleanField(default=True,verbose_name='Активен ли филиал')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'barbershop'
        ordering = ['is_active']

