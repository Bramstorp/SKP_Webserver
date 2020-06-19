from django.http import HttpResponse

from django.conf import settings

from django.shortcuts import render, redirect 

import datetime

from django.forms import inlineformset_factory

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from django.views.generic import View
 
# Create your views here.
from .forms import CreateUserForm
from .models import *

def homepage(request):
    nyt = Senestenyt.objects.all()

    context = {"nyt":nyt}
    return render(request, "skpcore/homepage.html", context)

def husregler(request):
    textform = Husreglerform.objects.all()

    context = {"textform":textform}
    return render(request, "skpcore/husregler.html", context)

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, "Username or Password is incorrect")
    context = {}
    return render(request, "skpcore/login.html", context)

def signuppage(request):
    form = CreateUserForm
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")

            messages.success(request, "account was created " + username)
            return redirect("loginpage")

    context = {"form":form}
    return render(request, "skpcore/signup.html", context)

def logoutUser(request):
    logout(request)
    return redirect('homepage')

def idekasse(request):
    blog = Blogpost.objects.all()

    context = {"blog":blog}
    return render(request, "skpcore/idekasse.html", context)

def ide(request,pk):
    blog = Blogpost.objects.get(id=pk)

    context = {"blog":blog}
    return render(request, "skpcore/ide.html", context)

def info(request):
    textform = Infoform.objects.all()

    context = {"textform":textform}
    return render(request, "skpcore/info.html", context)