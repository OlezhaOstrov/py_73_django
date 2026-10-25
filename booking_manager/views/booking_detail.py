from django.shortcuts import render, get_object_or_404
from booking_manager.models.booking import Booking

def booking_detail(request,booking_id):
    booking = get_object_or_404(
        Booking.objects.select_related('client','barber','booking_service')
        .prefetch_related('product_items__product'),
        id = booking_id)
    return render(request, 'booking_detail.html', {'booking':booking})