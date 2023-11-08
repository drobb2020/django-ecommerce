from django.shortcuts import render


def cart_summary(request):
    context = {}
    return render(request, 'cart/cart_summary.html', context)


def cart_add(request):
    pass


def cart_delete(request):
    pass


def cart_update(request):
    pass
