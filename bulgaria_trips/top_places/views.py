from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from bulgaria_trips.top_places.models import Place


class PlaceListView(ListView):
    model = Place
    template_name = 'places/list-place.html'
    context_object_name = 'places'


class PlaceCreateView(CreateView):
    model = Place
    template_name = 'places/create-place.html'
    success_url = reverse_lazy('list places')
    fields = ['Name', 'Beschreibung', 'Bezeichnung', 'Bild', 'user']


class PlaceUpdateView(UpdateView):
    model = Place
    template_name = 'places/udate-place.html'
    fields = ['Name', 'Beschreibung', 'Bezeichnung', 'Bild']
    success_url = reverse_lazy('list places')


# class PlaceDetailsView(DetailView):
#     model = Place
#     template_name = 'places/details-place.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['is_owner'] = self.object
#         return context

def places_details(request, pk):
    place = Place.objects.get(pk=pk)
    is_owner = place.user == request.user
    context = {
        'place': place,
        'is_owner': is_owner,
    }

    return render(request, 'places/details-place.html', context)


class PlaceDeleteView(DeleteView):
    model = Place
    template_name = 'places/delete-place.html'
    success_url = reverse_lazy('index')

