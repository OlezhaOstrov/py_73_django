from django.urls import path
from booking_manager.views.bookings import bookings
from booking_manager.views.new_booking import new_booking
from booking_manager.views.services import services
from booking_manager.views.home import home
from booking_manager.views.specialists import specialists
from booking_manager.views.booking_detail import booking_detail

urlpatterns = [
    path('', home, name='home'),
    path('services/',services,name='services'),
    path('specialists/',specialists,name='specialists'),
    path('bookings/',bookings,name='bookings'),
    path('new-booking/',new_booking,name='new booking'),
    path('bookings/<int:booking_id>/',booking_detail,name='booking_detail'),
]