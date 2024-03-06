# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import ShippingAddress


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'full_name',
        'email',
        'address1',
        'address2',
        'city',
        'state',
        'postal_code',
        'country',
    )
    list_filter = ('user',)
