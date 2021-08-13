from django.contrib.auth import logout, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from bulgaria_trips.accounts.forms import SignInForm, SignUpForm, ProfileForm
from bulgaria_trips.accounts.models import Profile
from django.contrib import messages


def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')

    else:
        form = SignUpForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/sign-up.html', context)


def sign_in(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = SignInForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts/sign-in.html', context)


def sign_out(request):
    logout(request)
    return redirect('index')


def profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'accounts/user-profile.html', context)


# def delete_profile(request, pk):
#     profile = Profile.objects.get(pk=pk)
#     if request.method == "POST":
#         profile.delete()
#         return redirect('index')
#     else:
#         context = {
#             'profile': profile,
#         }
#
#     return render(request, 'accounts/delete-profile.html', context)


# def delete_profile(request):
#     if request.method == "POST":
#         delete_form = ProfileDeleteForm(request.POST, instance=request.user)
#         user = request.user
#         user.delete()
#         return redirect('index')
#     else:
#         delete_form = ProfileDeleteForm(instance=request.user)
#
#     context = {
#         'delete_form': delete_form,
#     }
#
#     return render(request, 'accounts/delete-profile.html', context)


class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'accounts/delete-profile.html'
    success_url = reverse_lazy('index')
