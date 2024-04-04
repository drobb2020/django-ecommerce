from django import forms

from .models import ShippingAddress


class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(
        label="Full Name",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Full Name"}
        ),
        required=True,
    )
    shipping_email = forms.CharField(
        label="Full Name",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}),
        required=True,
    )
    shipping_address1 = forms.CharField(
        label="Address 1",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Address 1"}
        ),
        required=True,
    )
    shipping_address2 = forms.CharField(
        label="Address 2",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Address 2"}
        ),
        required=True,
    )
    shipping_city = forms.CharField(
        label="City",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "City"}),
        required=True,
    )
    shipping_state = forms.CharField(
        label="State | Province",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "State|Province"}
        ),
        required=True,
    )
    shipping_postal_code = forms.CharField(
        label="Postal Code",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Postal Code"}
        ),
        required=True,
    )
    shipping_country = forms.CharField(
        label="Country",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Country"}
        ),
        required=True,
    )

    class Meta:
        model = ShippingAddress
        fields = (
            "shipping_full_name",
            "shipping_email",
            "shipping_address1",
            "shipping_address2",
            "shipping_city",
            "shipping_state",
            "shipping_postal_code",
            "shipping_country",
        )
