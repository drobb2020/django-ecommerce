from django.contrib import admin

from .models import Category, Customer, Order, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {"slug": ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
