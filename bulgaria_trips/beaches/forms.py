from django import forms
from bulgaria_trips.core.forms import BootstrapFormMixin

from bulgaria_trips.beaches.models import Beach


class BeachForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Beach
        exclude = ('user',)
