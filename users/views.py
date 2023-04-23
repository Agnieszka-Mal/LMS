from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages

from users import forms


# Create your views here.
def logout_view(request):
    logout(request)
    return redirect(reverse('home:home'))

def registration_view(request):
    form = forms.RegistrationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            messages.add_message(request, messages.WARNING, f"You are registered. Please Login")
            form.save()

            return redirect(reverse('login'))

    return render(request, 'users/registration.html', {'form': form})

def login_user_view(request):
    if request.method == 'POST':
        form = forms.LoginForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(email=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.add_message(request, messages.SUCCESS, f"You are logged in. Hello {username}")
                    return redirect(reverse_lazy('home:home'))
    else:
        form = forms.LoginForm()
    return render(request, 'users/login.html', {'form': form})

