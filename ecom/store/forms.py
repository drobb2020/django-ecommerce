from django import forms
from django.contrib.auth.forms import SetPasswordForm, UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Email Address"}
        ),
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "Pick a User Name"
        self.fields["username"].label = ""
        self.fields[
            "username"
        ].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "Enter a Password"
        self.fields["password1"].label = ""
        self.fields[
            "password1"
        ].help_text = "<ul class=\"form-text text-muted small\"><li>Your password can't be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can't be a commonly used password.</li><li>Your password can't be entirely numeric.</li></ul>"

        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"
        self.fields["password2"].label = ""
        self.fields[
            "password2"
        ].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class UpdateProfileForm(UserChangeForm):
    password = None
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Email Address"}
        ),
        required=False,
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
        required=False,
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
        required=False,
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
        )

    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "Pick a User Name"
        self.fields["username"].label = ""
        self.fields[
            "username"
        ].help_text = '<span class="form-text text-muted"><small>Required. Up to 150 characters. Letters, digits and symbols (@/./+/-/_) only.</small></span>'


class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ["new_password1", "new_password2"]

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

        self.fields["new_password1"].widget.attrs["class"] = "form-control"
        self.fields["new_password1"].widget.attrs["placeholder"] = "Enter new Password"
        self.fields["new_password1"].label = ""
        self.fields[
            "new_password1"
        ].help_text = "<ul class=\"form-text text-muted small\"><li>Your password can't be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can't be a commonly used password.</li><li>Your password can't be entirely numeric.</li></ul>"

        self.fields["new_password2"].widget.attrs["class"] = "form-control"
        self.fields["new_password2"].widget.attrs[
            "placeholder"
        ] = "Confirm new Password"
        self.fields["new_password2"].label = ""
        self.fields[
            "new_password2"
        ].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class UserInfoForm(forms.ModelForm):
    phone = forms.CharField(
        label="Phone Number",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone"}),
        required=False,
    )
    address1 = forms.CharField(
        label="Address 1",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Address 1"}
        ),
        required=False,
    )
    address2 = forms.CharField(
        label="Address 2",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Address 2"}
        ),
        required=False,
    )
    city = forms.CharField(
        label="City",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "City"}),
        required=False,
    )
    state = forms.CharField(
        label="State | Province",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "State|Province"}
        ),
        required=False,
    )
    zipcode = forms.CharField(
        label="Postal Code",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Postal Code"}
        ),
        required=False,
    )
    country = forms.CharField(
        label="Country",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Country"}
        ),
        required=False,
    )

    class Meta:
        model = Profile
        fields = (
            "phone",
            "address1",
            "address2",
            "city",
            "state",
            "zipcode",
            "country",
        )
