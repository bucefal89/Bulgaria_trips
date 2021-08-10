from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from bulgaria_trips.core.forms import BootstrapFormMixin
from bulgaria_trips.mountain.models import Mountain, Source


class MountainCreatView(CreateView):
    model = Mountain
    template_name = 'mountains/create-mountain.html'
    success_url = reverse_lazy('index')
    fields = ['Name', 'Bezeichnung', 'Bild', 'Name', 'source']


class MountainListView(ListView):
    model = Mountain
    template_name = 'mountains/list-mountain.html'
    context_object_name = 'mountains'


class MountainUpdateView(UpdateView):
    model = Mountain
    template_name = 'mountains/update-mountain.html'
    fields = ['Name', 'Bezeichnung', 'Bild', 'source']
    success_url = reverse_lazy('list mountains')


def mountain_details(request, pk):
    mountain = Mountain.objects.get(pk=pk)
    is_owner = mountain.user == request.user
    context = {
        'mountain': mountain,
        'is_owner': is_owner,
    }

    return render(request, 'mountains/details-mountain.html', context)


class MountainDeleteView(DeleteView):
    model = Mountain
    template_name = 'mountains/delete-mountain.html'
    success_url = reverse_lazy('index')




