from django.shortcuts import render
from booking_manager.models.booking_service import BookingService


def services(request):
    services = BookingService.objects.all()
    return render(request,'services.html',context={'services':services})