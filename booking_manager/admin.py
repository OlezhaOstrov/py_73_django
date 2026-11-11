from django.contrib import admin

from django.db.models import F

from booking_manager.models.booking import Booking
from booking_manager.models.booking_service import BookingService
from booking_manager.models.products import Product
from booking_manager.models.productbooking import ProductBooking
from booking_manager.models.comment import Comment
from booking_manager.models.barbershop import Barbershop
from booking_manager.models.promotion import Promotion

from account.models.barber import Barber
from account.models.client import Client



# Массовые действия

@admin.action(description='Опубликовать комментарии')
def publish_comments(modeladmin, request, queryset):
    queryset.update(is_published=True)


@admin.action(description='Скрыть комментарии')
def hide_comments(modeladmin, request, queryset):
    queryset.update(is_published=False)


@admin.action(description='Увеличить количество на 10')
def increase_quantity(modeladmin, request, queryset):
    queryset.update(quantity=F('quantity') + 10)


@admin.action(description='Активировать акции')
def activate_promotions(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description='Деактивировать акции')
def deactivate_promotions(modeladmin, request, queryset):
    queryset.update(is_active=False)


# Товары в бронировании

class ProductBookingInline(admin.TabularInline):
    model = ProductBooking
    extra = 1
    fields = ('product', 'quantity')


# Комментарии на странице барбера

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    fields = ('client', 'text', 'rating', 'is_published', 'booking')



# Бронирования

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    inlines = [ProductBookingInline]

    list_display = (
        'name',
        'visit_time',
        'is_active',
        'barber',
        'client',
        'booking_service',
        'booking_and_barber_name',
    )

    list_display_links = ('name', 'visit_time')
    list_editable = ('is_active',)

    readonly_fields = ('created_at', 'total_products_cost')

    fields = (
        'name',
        'visit_time',
        'is_active',
        'barber',
        'client',
        'booking_service',
        'created_at',
        'total_products_cost',
    )

    search_fields = (
        'name',
        'client__user__email',
        'barber__name',
    )

    list_filter = (
        'is_active',
        'visit_time',
        'barber',
        'booking_service',
    )

    @admin.display(description='Бронирование — барбер')
    def booking_and_barber_name(self, obj):
        return f'{obj.name} — {obj.barber.name}'

    @admin.display(description='Стоимость товаров')
    def total_products_cost(self, obj):
        total = 0

        for item in obj.product_items.select_related('product').all():
            total += item.quantity * item.product.price

        return total


# Товары

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_display_links = ('name',)
    list_editable = ('price',)
    search_fields = ('name',)


# Позиции товаров в бронированиях

@admin.register(ProductBooking)
class ProductBookingAdmin(admin.ModelAdmin):
    list_display = ('booking', 'product', 'quantity')
    list_editable = ('quantity',)
    actions = [increase_quantity]


# Барберы

@admin.register(Barber)
class BarberAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

    list_display = ('name', 'experience', 'barbershop', 'rating')
    search_fields = ('name',)


# Клиенты

admin.site.register(Client)


# Услуги

@admin.register(BookingService)
class BookingServiceAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')


# Филиалы

@admin.register(Barbershop)
class BarbershopAdmin(admin.ModelAdmin):
    search_fields = ('name', 'address')


# Комментарии

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'client',
        'text',
        'rating',
        'is_published',
    )

    list_filter = ('rating', 'is_published')
    actions = [publish_comments, hide_comments]


# Акции

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('name', 'discount_percent', 'start_date', 'end_time', 'is_active')
    list_filter = ('is_active',)
    actions = [activate_promotions, deactivate_promotions]
