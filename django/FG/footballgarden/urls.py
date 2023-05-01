from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("football/", views.football, name='football'),
    path("sport/", views.sport, name='sport'),
    path("", include('django.contrib.auth.urls')),
    path("signup/", views.signup, name='signup'),
]
