from django.db import models
from booking_manager.models.base import BaseModel
from booking_manager.constants import ClientChoices
from django.conf import settings


class Client(BaseModel):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11,unique=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='client')

    status = models.CharField(choices=ClientChoices,
                              max_length=10,
                              default=ClientChoices.NEW
                              )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'clients'
        verbose_name_plural = 'Клиент'
        ordering = ['-created_at','name']
