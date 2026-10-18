from django.urls import path
from booking_manager.views import home, specialists,services,bookings, new_booking

urlpatterns = [
    path('', home, name='home'),
    path('services/',services,name='services'),
    path('specialists/',specialists,name='specialists'),
    path('bookings/',bookings,name='bookings'),
    path('new-booking/',new_booking,name='new booking'),
]