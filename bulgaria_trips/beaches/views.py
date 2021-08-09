from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from bulgaria_trips.beaches.forms import BeachForm
from bulgaria_trips.beaches.models import Beach


def all_beach(request):
    all_beaches = Beach.objects.all()
    context = {
        'beaches': all_beaches,
    }

    return render(request, 'beaches/list-beaches.html', context)


@login_required
def create_beaches(request):
    if request.method == "POST":
        form = BeachForm(request.POST, request.FILES)
        if form.is_valid():
            beach = form.save(commit=False)
            beach.user = request.user
            beach.source = request.user
            beach.save()
            return redirect('all beaches')
    else:
        form = BeachForm()

    context = {
        'form': form,
    }

    return render(request, 'beaches/create-beaches.html', context)


def update_beaches(request, pk):
    pass


def details_beaches(request, pk):
    pass
    # beach = Beach.objects.get(pk)
    # context = {
    #     'beaches': beach,
    # }
    #
    # return render(request, 'beaches/details-beaches.html', context)


def delete_beaches(request, pk):
    pass