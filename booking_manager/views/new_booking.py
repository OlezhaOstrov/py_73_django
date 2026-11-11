from django.shortcuts import render,redirect
from booking_manager.forms import BookingForm
from account.models.client import Client
from django.contrib.auth.decorators import login_required



@login_required
def new_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False) #объект бронирования (конкретное бронирование
                                              #в виде Python объекта, у которого есть
                                              #booking.name, booking.booking_service
            client = Client.objects.get(user=request.user) # профиль клиента текущего пользователя
            booking.client = client #присваиваем профиль объекту бронирования
            booking.save()
            return redirect('bookings')
    else:
        form = BookingForm()
    return render(request, 'new_booking.html', {'form': form})
