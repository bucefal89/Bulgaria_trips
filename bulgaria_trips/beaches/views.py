from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView

from bulgaria_trips.beaches.forms import BeachForm
from bulgaria_trips.beaches.models import Beach


def all_beach(request):
    all_beaches = Beach.objects.all()
    context = {
        'beaches': all_beaches,
    }

    return render(request, 'beaches/list-beaches.html', context)


class BeachCreatView(CreateView):
    model = Beach
    template_name = 'beaches/create-beaches.html'
    success_url = reverse_lazy('all beaches')
    fields = ['Name', 'Bezeichnung', 'Bild', 'Name', 'source', 'user']

# @login_required
# def create_beaches(request):
#     if request.method == "POST":
#         form = BeachForm(request.POST, request.FILES)
#         if form.is_valid():
#             beach = form.save()
#             beach.user = request.user
#             beach.source = request.user
#             beach.save()
#             return redirect('all beaches')
#     else:
#         form = BeachForm()
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'beaches/create-beaches.html', context)


class BeachUpdateView(UpdateView):
    model = Beach
    template_name = 'beaches/update-beaches.html'
    fields = ['Name', 'Bezeichnung', 'Bild', 'source']
    success_url = reverse_lazy('all beaches')


def details_beaches(request, pk):
    beach = Beach.objects.get(pk=pk)
    is_owner = beach.user == request.user
    context = {
        'beach': beach,
        'is_owner': is_owner
    }

    return render(request, 'beaches/details-beaches.html', context)


def delete_beaches(request, pk):
    beach = Beach.objects.get(pk=pk)
    if request.method == "POST":
        beach.delete()
        return redirect('all beaches')
    else:
        context = {
            'beach': beach,
        }

    return render(request, 'beaches/delete-beaches.html', context)


