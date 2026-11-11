from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class RatingMixin(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    class Meta:
        abstract = True
