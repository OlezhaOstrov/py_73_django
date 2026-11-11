from django.urls import path

from booking_manager.views.bookings import bookings
from booking_manager.views.new_booking import new_booking
from booking_manager.views.services import services
from booking_manager.views.home import home
from booking_manager.views.specialists import specialists
from booking_manager.views.booking_detail import booking_detail
from booking_manager.views.productbooking import product_booking
from booking_manager.views.classviews import (
    AboutView,
    RulesBarbershopView,
    ContactView,
    BarbersView,
    RatingCreateView,
    ClientUpdateBookingView


)

urlpatterns = [
    path('', home, name='home'),
    path('services/',services,name='services'),
    path('specialists/',specialists,name='specialists'),
    path('bookings/',bookings,name='bookings'),
    path('new-booking/',new_booking,name='new booking'),
    path('bookings/<int:booking_id>/',booking_detail,name='booking_detail'),
    path('bookings/<int:booking_id>/product/add/',product_booking,name='product_booking'),
    path('about/',AboutView.as_view(),name='about'),
    path('contact/',ContactView.as_view(),name='contact'),
    path('rules/',RulesBarbershopView.as_view(),name='rules'),
    path('barber/<int:pk>/',BarbersView.as_view(),name='barber'),
    path('rating/',RatingCreateView.as_view(),name='rating'),
    path('bookings/<int:pk>/edit',ClientUpdateBookingView.as_view(),name='ClientUpdateBooking')
]