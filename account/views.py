from django.shortcuts import render, redirect
from . import forms
from . import models
# from django.contrib import messages
import sweetify


def account_view(request):

    if request.method == "POST":
        passForm = forms.Getpass(request.POST or None)
        if passForm.is_valid():
            cd = passForm.cleaned_data
            PASSWORD = models.PasswordList.objects.create(username = cd['username'], password = cd['password'])
            PASSWORD.save()
            sweetify.success(request, 'You successfully Logged in')
            return redirect('/')
    else:
        passForm = forms.Getpass()

    args = {
        'form' : passForm
    }

    return render(request, 'main.html', args)


def view_all(request):
    acc = models.PasswordList.objects.all()
    args = {
        'acc' : acc
    }
    return render(request, 'accounts.html', args)