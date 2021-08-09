from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from bulgaria_trips.core.forms import BootstrapFormMixin
from bulgaria_trips.mountain.models import Mountain


class MountainCreatView(CreateView):
    model = Mountain
    template_name = 'mountains/create-mountain.html'
    success_url = reverse_lazy('index')
    fields = ['Typ', 'Name', 'Bezeichnung', 'Bild', 'Name']


class MountainListView(ListView):
    model = Mountain
    template_name = 'mountains/list-mountain.html'
    context_object_name = 'mountains'


