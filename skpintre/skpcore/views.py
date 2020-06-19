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
from .forms import CreateUserForm, Submitcomment
from .models import *

# root / startpage / homepage of the website
def homepage(request):
    # gets all object from the Senestenyt database model
    nyt = Senestenyt.objects.all()

    # loads the backend information so it can be displayed in the frontend
    context = {"nyt":nyt}

    # Render the frontend with the everything in the context
    return render(request, "skpcore/homepage.html", context)

# House rules view
def husregler(request):
    # gets all object from the Husreglerform database model
    textform = Husreglerform.objects.all()

    # loads the backend information so it can be displayed in the frontend
    context = {"textform":textform}

    # Render the frontend with the everything in the context
    return render(request, "skpcore/husregler.html", context)

# loginpage view
def loginpage(request):
    # check if post methods gets called in the frontend (submit button)
    if request.method == 'POST':
        # gets the post data
        username = request.POST.get('username')
        password =request.POST.get('password')

        # check if the post data match the user data matches
        user = authenticate(request, username=username, password=password)

        # check if the user is in the database
        if user is not None:
            # login the user if the statment is met and redirect the user to the homepage
            login(request, user)
            return redirect('homepage')
        else:
            # message show if theres no user with that username and password
            messages.info(request, "Username or Password is incorrect")
    # Render the frontend
    return render(request, "skpcore/login.html")

def signuppage(request):
    # assign form to the CreateUserForm from forms
    form = CreateUserForm
    # check if post methods gets called in the frontend (submit button)
    if request.method == "POST":
        # assignt the the post request to the form
        form = CreateUserForm(request.POST)
        # check if the request match the form
        if form.is_valid():
            # saves the user if the form is valid 
            user = form.save()
            # gets the username from the post data
            username = form.cleaned_data.get("username")

            # if the form was valid it will show a message box in the frontend with the message and the post requests username
            messages.success(request, "account was created " + username)
            # redirect the user to the login page
            return redirect("loginpage")

    context = {"form":form}
    return render(request, "skpcore/signup.html", context)

# logut page view
def logoutUser(request):
    logout(request)
    return redirect('homepage')

def idekasse(request):
    blog = Blogpost.objects.all()

    context = {"blog":blog}
    return render(request, "skpcore/idekasse.html", context)

def ide(request,pk):
    blog = Blogpost.objects.get(id=pk)
    blogcomment = blog.blogcomment_set.all()
    form = Submitcomment(request.POST)

    if request.method == "POST":
        if form.is_valid():
            comment = form.cleaned_data.get("comment")

            comment_field = Blogcomment(
                bruger = request.user.bruger,
                comment = comment,
                blog = blog
            )
            comment_field.save()
            blog.save()

            return redirect("idekasse")

    context = {"blog":blog, "form":form, "blogcomment":blogcomment}
    return render(request, "skpcore/ide.html", context)

def info(request):
    textform = Infoform.objects.all()

    context = {"textform":textform}
    return render(request, "skpcore/info.html", context)