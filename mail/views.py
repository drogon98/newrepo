from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


def home(request):
    users = User.objects.all().order_by('-date_joined')
    args = {'users': users}
    return render(request, 'mail/home.html', args)
