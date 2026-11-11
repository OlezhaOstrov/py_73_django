from django.db import models
from django.utils import timezone

class BookingManager(models.Manager):

    def active_upcoming(self):
        current_time = timezone.localtime().now()
        return self.get_queryset().filter(is_active=True, visit_time__gte=current_time)