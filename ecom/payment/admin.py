# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import ShippingAddress, Order, OrderItem


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'shipping_full_name',
        'shipping_email',
        'shipping_address1',
        'shipping_address2',
        'shipping_city',
        'shipping_state',
        'shipping_postal_code',
        'shipping_country',
    )
    list_filter = ('user',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'full_name',
        'email',
        'shipping_address',
        'amount_paid',
        'date_ordered',
    )
    list_filter = ('user', 'date_ordered')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'user', 'quantity', 'price')
    list_filter = ('order', 'product', 'user')
