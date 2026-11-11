from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from booking_manager.models.booking_service import BookingService
from account.models.barber import Barber
from booking_manager.models.comment import Comment
from account.models.client import Client
from booking_manager.models.booking import Booking


#Задание 1
class AboutView(TemplateView):
    template_name='about.html'

class ContactView(TemplateView):
    template_name='contact.html'

class RulesBarbershopView(TemplateView):
    template_name='rulesbarbershop.html'



#Задание 2
class BookingServiceView(ListView):
    template_name='bookingservice.html'
    context_object_name = 'bookings_service'
    model = BookingService
    def get_queryset(self):
        return BookingService.objects.filter(is_active=True)


#Задание 3
class BarbersView(DetailView):
    template_name='barbers.html'
    context_object_name = 'barber'
    model = Barber

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comment.filter(
            is_published=True
        ).order_by('-created_at')[:5]
        return context

#Задание 4
class RatingCreateView(CreateView):
    template_name='rating_create.html'
    model = Comment
    success_url = reverse_lazy('specialists')
    fields = ['rating','text']
    def form_valid(self, form):
        form.instance.client = Client.objects.get(user=self.request.user)
        return super().form_valid(form)


#Задание 5
class ClientUpdateBookingView(UpdateView):
    template_name = 'booking_edit.html'
    model = Booking
    fields = ['visit_time','booking_service']
    success_url = reverse_lazy('bookings')

    def get_queryset(self):
        return Booking.objects.filter(
            client__user=self.request.user,
            is_active=True
        )

#Задание 6
class CommentsDeleteView(DeleteView):
    model = Comment
    context_object_name = 'comments'
    success_url = reverse_lazy('specialists')

    def get_queryset(self):
        return Comment.objects.filter(client__user=self.request.user)

