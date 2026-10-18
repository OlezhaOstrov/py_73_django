from django.contrib import admin

from account.models import Barber,Client
admin.site.register(Barber)
admin.site.register(Client)