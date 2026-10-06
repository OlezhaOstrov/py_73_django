from django.db import models
from booking_manager.constants import CategoryChoices

class Booking(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='Название',
                            )
    price = models.FloatField(verbose_name='Цена',
                              null=True,
                              blank=True)
    category = models.CharField(max_length=100,
                                default=CategoryChoices.HAIRCUT,
                                choices=CategoryChoices,
                                verbose_name='Категория'
                                )
    visit_time = models.TimeField(null=True,blank=True,verbose_name='Время визита')
    is_active = models.BooleanField(default=True,verbose_name='Активно')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Обновленная запись')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'booking'
        ordering = ['-created_at']

