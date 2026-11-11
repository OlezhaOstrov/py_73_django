from django import forms
from django.forms.widgets import NumberInput
from account.models.barber import Barber
from booking_manager.models.booking import  Booking
from django.utils import timezone
from django.core.exceptions import ValidationError
from booking_manager.models.booking_service import BookingService
from booking_manager.models.productbooking import ProductBooking


class CommentForm(forms.Form):
    barber = forms.ModelChoiceField(queryset=Barber.objects.all(),
                                    label='барбер'
                                    )
    rating = forms.IntegerField(widget=NumberInput(),
                                min_value=1,
                                max_value=5,
                                label='Оценка'
                                )
    text = forms.CharField(widget=forms.Textarea(),
                           label='Текст'
                           )



class BookingForm(forms.ModelForm):
    def clean_visit_time(self):
        visit_time = self.cleaned_data.get('visit_time')
        if visit_time < timezone.now():
            raise ValidationError('Нельзя записаться на прошедшие дату и время.')
        return visit_time

    def clean(self):
        cleaned_data = super().clean() #cleaned_data - словарь питон в котором хранится информация формы
        barber = cleaned_data.get('barber')
        visit_time = cleaned_data.get('visit_time')
        if visit_time and barber:
            if Booking.objects.filter(barber=barber,
                                      visit_time=visit_time,
                                      is_active=True
                                      ).exists():
                raise ValidationError('Барбер уже занят на это время')
        return cleaned_data

    class Meta:
        model = Booking
        fields = ('visit_time','booking_service','barber')



class BookingServiceForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        price = cleaned_data.get('price')
        duration_minutes = cleaned_data.get('duration_minutes')
        if price is not None and price <= 0:
            self.add_error('price', 'Цена должна быть больше нуля')
        if duration_minutes is not None and duration_minutes <= 0:
            self.add_error('duration_minutes', 'Продолжительность должна быть больше нуля', )
        return cleaned_data

    class Meta:
        model = BookingService
        fields = ('name','category','description','price','duration_minutes','is_active')
        widgets = {'description': forms.Textarea(),}


class ProductBookingForm(forms.ModelForm):
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')
        if quantity <= 0:
            raise forms.ValidationError ('Количество должно быть больше нуля')
        if product and quantity > product.stock_quantity:
            raise forms.ValidationError (f'На складе осталось только {product.stock_quantity}')
        return quantity
    class Meta:
        model = ProductBooking
        fields = ('product','quantity')

