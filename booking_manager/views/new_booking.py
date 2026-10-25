from django.shortcuts import render

def new_booking(request):
    return render(request,'new_booking.html')