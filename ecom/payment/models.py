from django.contrib.auth.models import User
from django.db import models


class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, blank=True, default="N/A")
    postal_code = models.CharField(max_length=20, blank=True, default="N/A")
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"Shipping Address - {self.user.username}"

    class Meta:
        verbose_name_plural = "Shipping Address"
