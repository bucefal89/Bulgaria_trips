from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from bulgaria_trips.core.forms import BootstrapFormMixin


class SignInForm(BootstrapFormMixin, forms.Form):
    user = None
    email = forms.CharField(
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )

    def clean_password(self):
        self.user = authenticate(
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
        )

        if not self.user:
            raise ValidationError('Email or password incorrect')

    def save(self):
        return self.user
