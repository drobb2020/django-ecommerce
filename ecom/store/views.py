import json

from cart.cart import Cart
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect, render
from payment.forms import ShippingForm
from payment.models import ShippingAddress

from .forms import ChangePasswordForm, SignUpForm, UpdateProfileForm, UserInfoForm
from .models import Category, Product, Profile


def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "store/home.html", context)


def product(request, pk):
    product = Product.objects.get(id=pk)
    context = {"product": product}
    return render(request, "store/product.html", context)


def category(request, slug):
    try:
        category = Category.objects.get(slug=slug)
        products = Product.objects.filter(category=category)
        context = {"products": products, "category": category}
        return render(request, "store/category.html", context)
    except:  # noqa: E722
        messages.success(request, "That category does not exist, try again.")
        return redirect("home")


def about(request):
    context = {}
    return render(request, "store/about.html", context)


def contact(request):
    context = {}
    return render(request, "store/contact.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user = Profile.objects.get(user__id=request.user.id)
            saved_cart = current_user.old_cart
            if saved_cart:
                converted_cart = json.loads(saved_cart)
                cart = Cart(request)
                for key, value in converted_cart.items():
                    cart.db_add(product=key, quantity=value)
            messages.success(request, "You have been logged in. Welcome!")
            return redirect("home")
        else:
            messages.error(request, "There was an error, please try again.")
            return redirect("login")
    else:
        return render(request, "store/login.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have logged out. See you next time!")
    return redirect("login")


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request,
                "Great, your account is successfully registered. Please complete your personal information.",
            )
            return redirect("update-user-info")
        else:
            messages.error(
                request,
                "Oops something went wrong with your registration, please try again.",
            )
            return redirect("register")
    else:
        context = {"form": form}
        return render(request, "store/register.html", context)


def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateProfileForm(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, "Your profile was updated successfully.")
            return redirect("home")
        return render(request, "store/update_user.html", {"user_form": user_form})
    else:
        messages.error(request, "You must be authenticated to access this page!")
        return redirect("home")


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(
                    request, "Your password has been updated. Enjoy your experience"
                )
                login(request, current_user)
                return redirect("update-user")
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)
                    return redirect("update_password")
        else:
            form = ChangePasswordForm(current_user)
            context = {"form": form}
            return render(request, "store/update_password.html", context)
    else:
        messages.error(request, "You must be authenticated to access this page!")
        return redirect("home")


def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        form = UserInfoForm(request.POST or None, instance=current_user)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)

        if form.is_valid() or shipping_form.is_valid():
            form.save()
            shipping_form.save()

            messages.success(
                request, "Your Billing & Shipping information was updated successfully."
            )
            return redirect("home")
        return render(
            request,
            "store/update_info.html",
            {"form": form, "shipping_form": shipping_form},
        )
    else:
        messages.info(request, "You must be authenticated to access this page!")
        return redirect("home")


def search(request):
    if request.method == "POST":
        searched = request.POST["q"]
        searched = Product.objects.filter(
            Q(name__icontains=searched) | Q(description__icontains=searched)
        )
        if not searched:
            messages.info(request, "That product does not exist, please try again.")
            return render(request, "store/search.html", {})
        else:
            context = {"searched": searched}
            return render(request, "store/search.html", context)
    else:
        context = {}
        return render(request, "store/search.html", context)
