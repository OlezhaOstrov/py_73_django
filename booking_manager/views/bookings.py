from django.shortcuts import render
from booking_manager.models import Booking


def bookings(request):
    bookings = Booking.objects.select_related('client','barber','booking_service').filter(client__user=request.user)
    return render(request, 'bookings.html', context={'bookings': bookings})



