from audioop import reverse

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import forms

from django.urls import reverse


# Create your views here.
def home(request):
    ctx = 'Hello'
    return render(request, 'home/index.html', context={
        'ctx': ctx
    })


def contact(request):
    form = forms.ContactMessageForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('home:home'))

    return render(request, "home/contact.html", {"form": form})
