from django.db import models
class CategoryChoices(models.TextChoices):
    HAIRCUT = 'haircut','Стрижка волос'
    MASSAGE = 'massage','Массаж'
    MUSTACHE = 'mustache', 'Стрижка усов'
    BEARD = 'beard', 'Стрижка бороды'

class ClientChoices(models.TextChoices):
    NEW = 'new','Новый клиент'
    REGULAR = 'regular','Постоянный'
    VIP = 'vip','Vip-клиент'

