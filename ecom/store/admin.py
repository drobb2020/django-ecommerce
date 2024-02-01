# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import User

from .models import Category, Customer, Order, Product, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "date_modified",
        "phone",
        "address1",
        "address2",
        "city",
        "state",
        "zipcode",
        "country",
    )
    list_filter = ("user", "date_modified")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ["name"]}


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "phone",
        "email",
        "password",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "price",
        "category",
        "description",
        "image",
        "is_sale",
        "sale_price",
    )
    list_filter = ("category", "is_sale")
    search_fields = ("name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "customer",
        "quantity",
        "address",
        "phone",
        "date",
        "status",
    )
    list_filter = ("product", "customer", "date", "status")


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    field = (
        "username",
        "first_name",
        "last_name",
        "email",
    )
    inlines = [ProfileInline]


admin.site.unregister(User)


admin.site.register(User, UserAdmin)
