from django.contrib.auth import logout, login
from django.shortcuts import render, redirect

from bulgaria_trips.accounts.forms import SignInForm, SignUpForm


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


