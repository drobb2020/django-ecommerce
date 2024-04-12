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
        required=False,
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


class PaymentForm(forms.Form):
    card_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Name on card"}
        ),
        required=True,
    )
    card_number = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Number"}
        ),
        required=True,
    )
    card_expiry_date = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Expiration Date"}
        ),
        required=True,
    )
    card_ccv_number = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "cvv number"}
        ),
        required=True,
    )
    card_address1 = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Address 1"}
        ),
        required=True,
    )
    card_address2 = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Address 2"}
        ),
        required=False,
    )
    card_city = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "City"}
        ),
        required=True,
    )
    card_state = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "State | Province"}
        ),
        required=True,
    )
    card_postal_code = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Postal Code"}
        ),
        required=True,
    )
    card_country = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Country"}
        ),
        required=True,
    )
