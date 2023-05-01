from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def home(request):
    context = {"message": "Hello World"}
    template = loader.get_template("footballgarden/html/index.html")
    return HttpResponse(template.render(context, request))


def football(request):
    context = {"message": "Hello World"}
    template = loader.get_template("footballgarden/html/football.html")
    return HttpResponse(template.render(context, request))


def sport(request):
    context = {"message": "Hello World"}
    template = loader.get_template("footballgarden/html/sport.html")
    return HttpResponse(template.render(context, request))


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })
