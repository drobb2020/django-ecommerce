from django.shortcuts import render


def payment_success(request):
    context = {}
    return render(request, "payment/payment_success.html", context)
