import datetime

from cart.cart import Cart
from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import PaymentForm, ShippingForm
from .models import Order, OrderItem, ShippingAddress
from store.models import Profile


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


def billing_info(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total()

        # Create a session with shipping info
        my_shipping = request.POST
        request.session["my_shipping"] = my_shipping
        if request.user.is_authenticated:
            billing_form = PaymentForm()
            context = {
                "cart_products": cart_products,
                "quantities": quantities,
                "totals": totals,
                "shipping_addr": request.POST,
                "billing_addr": billing_form,
            }
            return render(request, "payment/billing.html", context)
        else:
            billing_form = PaymentForm()
            context = {
                "cart_products": cart_products,
                "quantities": quantities,
                "totals": totals,
                "shipping_addr": request.POST,
                "billing_addr": billing_form,
            }
            return render(request, "payment/billing.html", context)

        context = {
            "cart_products": cart_products,
            "quantities": quantities,
            "totals": totals,
            "shipping_addr": request.POST,
        }
        return render(request, "payment/billing.html", context)
    else:
        messages.warning(request, "Access Denied!")
        return redirect("home")


def process_order(request):
    if request.POST:
        # Get the Cart
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total()

        # Get billing information
        # payment_form = PaymentForm(request.POST or None)

        # Get shipping session data
        my_shipping = request.session.get("my_shipping")

        # Gather order information
        full_name = my_shipping["shipping_full_name"]
        email = my_shipping["shipping_email"]

        # create shipping address from session info
        shipping_address = f"{my_shipping['shipping_address1']}\n{my_shipping['shipping_address2']}\n{my_shipping['shipping_city']}, {my_shipping['shipping_state']}, {my_shipping['shipping_postal_code']}\n{my_shipping['shipping_country']}"
        amount_paid = totals

        # Create an Order
        if request.user.is_authenticated:
            # Logged in
            user = request.user
            # Create order
            create_order = Order(
                user=user,
                full_name=full_name,
                email=email,
                shipping_address=shipping_address,
                amount_paid=amount_paid,
            )
            create_order.save()

            # Add order items
            # Get the order ID
            order_id = create_order.pk

            # Get product info
            for product in cart_products():
                # Get product ID
                product_id = product.id
                # Get product price
                if product.is_sale:
                    price = product.sale_price
                else:
                    price = product.price
                # Get quantity
                for key, value in quantities().items():
                    if int(key) == product.id:
                        # Create order item
                        create_order_item = OrderItem(
                            order_id=order_id,
                            product_id=product_id,
                            user=user,
                            quantity=value,
                            price=price,
                        )
                        create_order_item.save()
            # Delete cart
            for key in list(request.session.keys()):
                if key == "session_key":
                    # Delete the key
                    del request.session[key]

            # Delete Cart from Database (old cart field)
            current_user = Profile.objects.filter(user__id=request.user.id)
            # Delete shopping cart in db
            current_user.update(old_cart="")

            messages.success(request, "Order successfully placed!")
            return redirect("home")
        else:
            # Not logged in
            # Create order
            create_order = Order(
                full_name=full_name,
                email=email,
                shipping_address=shipping_address,
                amount_paid=amount_paid,
            )
            create_order.save()
            # Add order items
            # Get the order ID
            order_id = create_order.pk

            # Get product info
            for product in cart_products():
                # Get product ID
                product_id = product.id
                # Get product price
                if product.is_sale:
                    price = product.sale_price
                else:
                    price = product.price
                # Get quantity
                for key, value in quantities().items():
                    if int(key) == product.id:
                        # Create order item
                        create_order_item = OrderItem(
                            order_id=order_id,
                            product_id=product_id,
                            quantity=value,
                            price=price,
                        )
                        create_order_item.save()
            # Delete cart
            for key in list(request.session.keys()):
                if key == "session_key":
                    # Delete the key
                    del request.session[key]

            messages.success(
                request,
                "Order successfully placed! You should consider creating an account for faster checkouts.",
            )
            return redirect("home")
    else:
        messages.warning(request, "Access Denied!")
        return redirect("home")


def dashboard_shipped(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders = Order.objects.filter(shipped=True)
        if request.POST:
            # status = Order.objects.filter(shipped=True)
            num = request.POST['num']
            order = Order.objects.filter(id=num)
            order.update(shipped=False)
            messages.success(request, "Shipping status updated!")
            return redirect("home")
        context = {"orders": orders}
        return render(request, "payment/dashboard_shipped.html", context)
    else:
        messages.success(request, "Order Shipped!")
        return redirect("home")


def dashboard_outstanding(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders = Order.objects.filter(shipped=False)
        if request.POST:
            # status = request.POST['shipping_status']
            num = request.POST['num']
            # Get the order
            order = Order.objects.filter(id=num)
            # Grab current date and time
            now = datetime.datetime.now()
            # Update order
            order.update(shipped=True, date_shipped=now)
            # Message and redirect
            messages.success(request, "Shipping status updated!")
            return redirect("home")
        context = {"orders": orders}
        return render(request, "payment/dashboard_outstanding.html", context)
    else:
        messages.success(request, "Order Requires Shipping!")
        return redirect("home")


def orders(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        # Get the order
        order = Order.objects.get(id=pk)
        # Get the order items
        items = OrderItem.objects.filter(order=pk)
        if request.POST:
            status = request.POST["shipping_status"]
            # Check if true or false
            if status == "true":
                # get the order
                order = Order.objects.filter(id=pk)
                # Update the status and date shipped
                now = datetime.datetime.now()
                order.update(shipped=True, date_shipped=now)
            else:
                # Get the order
                order = Order.objects.filter(id=pk)
                # Update the status
                order.update(shipped=False)
            messages.success(request, "Shipping status updated!")
            return redirect("home")
        context = {"order": order, "items": items}
        return render(request, "payment/orders.html", context)
    else:
        messages.warning(request, "Access Denied!")
        return redirect("home")
