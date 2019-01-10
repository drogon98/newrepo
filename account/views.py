from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import UserRegisterForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST) # binding the form with the user data
        if form.is_valid():
            # print(form.errors)
            # print(form.is_valid()) if True the data is valid
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Welcome { username },your account has been successfully created!")
            return redirect('login')
    else:
        form = UserRegisterForm()
        print(form)
    args = {'form': form}
    return render(request, 'account/register.html', args)
