from django.shortcuts import render

# Create your views here.
from .forms import HusreglForm
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
    context = {}
    return render(request, "skpcore/login.html", context)

def signuppage(request):
    context = {}
    return render(request, "skpcore/signup.html", context)

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