from booking_manager.forms import ProductBookingForm
from django.shortcuts import render,redirect,get_object_or_404
from booking_manager.models import Booking




def product_booking(request,booking_id):
    booking = get_object_or_404(Booking, id = booking_id)
    if request.method == 'POST':
        form = ProductBookingForm(request.POST)
        if form.is_valid():
            product_booking = form.save(commit=False)
            product_booking.booking = booking
            product_booking.total_price = product_booking.quantity * product_booking.product.price
            product_booking.save()
            return redirect('bookings')
    else:
        form = ProductBookingForm()
    return render(request, 'product_booking.html', {'form': form},)