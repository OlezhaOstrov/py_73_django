from django.apps import AppConfig


class BookingManagerConfig(AppConfig):
    name = 'booking_manager'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        import booking_manager.signals