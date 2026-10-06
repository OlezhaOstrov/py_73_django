from django.db import models
class CategoryChoices(models.TextChoices):
    HAIRCUT = 'haircut'
    MASSAGE = 'massage'
    MUSTACHE = 'mustache'
    BEARD = 'beard'