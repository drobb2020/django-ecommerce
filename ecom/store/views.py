from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from .forms import ChangePasswordForm, SignUpForm, UpdateProfileForm
from .models import Category, Product


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
    except:
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
            messages.success(request, "You have been logged in. Welcome!")
            return redirect("home")
        else:
            messages.warning(request, "There was an error, please try again.")
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
            messages.success(request, "Great, your account is successfully registered.")
            return redirect("home")
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
        messages.success(request, "You must be authenticated to access this page!")
        return redirect("home")


def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been updated. Enjoy your experience")
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
