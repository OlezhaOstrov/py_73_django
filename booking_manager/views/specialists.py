from account.models import Barber
from django.shortcuts import render

def specialists(request):
    barbers = Barber.objects.prefetch_related('comment')
    return render(request, 'specialists.html', {'barbers': barbers})
