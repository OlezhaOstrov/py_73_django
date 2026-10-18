from django.db import models
from booking_manager.models.base import BaseModel
from account.models.client import Client
from account.models.barber import Barber
class Comment(BaseModel):
    text = models.TextField(verbose_name='Текст комментария')
    rating = models.PositiveIntegerField(null=True,verbose_name='')
    is_published = models.BooleanField(default=True)
    client = models.ForeignKey(to=Client,
                                  on_delete=models.SET_NULL,
                                  related_name='comment',
                                  null=True,
                                  verbose_name='Автор комментария')
    barber = models.ForeignKey(to=Barber,
                                  on_delete=models.SET_NULL,
                                  related_name='comment',
                                  null=True,
                                  verbose_name='Барбер, которому оставлен отзыв')
    booking = models.OneToOneField(to='Booking',
                                   unique=True,
                                   on_delete=models.SET_NULL,
                                   related_name='comment',
                                   null=True,
                                   verbose_name='Бронирование, которому оставили отзыв'
                                   )
    def __str__(self):
        return self.text

    class Meta:
        db_table = 'comment'
        ordering = ['-created_at']
        verbose_name = 'Комментарий'
