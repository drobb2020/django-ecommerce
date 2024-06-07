from django.urls import path

from . import views

urlpatterns = [
    path('payment_success/', views.payment_success, name='payment-success'),
    path("checkout/", views.checkout, name='checkout'),
    path("billing_info/", views.billing_info, name="billing_info"),
    path("process_order/", views.process_order, name="process_order"),
    path("shipped/", views.dashboard_shipped, name="dashboard_shipped"),
    path("outstanding/", views.dashboard_outstanding, name="dashboard_outstanding"),
    path("orders/<int:pk>/", views.orders, name="orders"),
]
