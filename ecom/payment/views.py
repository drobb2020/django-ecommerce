from cart.cart import Cart
from django.shortcuts import render

from .forms import ShippingForm
from .models import ShippingAddress


def payment_success(request):
    context = {}
    return render(request, "payment/payment_success.html", context)


def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    if request.user.is_authenticated:
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        context = {
            "cart_products": cart_products,
            "quantities": quantities,
            "totals": totals,
            "shipping_form": shipping_form,
        }
        return render(request, "payment/checkout.html", context)
    else:
        # Checkout as a guest
        shipping_form = ShippingForm(request.POST or None)
        context = {
            "cart_products": cart_products,
            "quantities": quantities,
            "totals": totals,
            "shipping_form": shipping_form,
        }
        return render(request, "payment/checkout.html", context)
