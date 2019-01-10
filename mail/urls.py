from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="mail_home"),
]
