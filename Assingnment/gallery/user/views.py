from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render (request,"user/index.html")

def about(request):
    return render(request, "user/about.html")

def register(request):
    if request.method=="POST":
        reg_form=UserCreationForm(request.POST)
        if reg_form.is_valid():
            user=reg_form.save()
            messages.success(request,f'Registered Successfully')
            return redirect ("login")

    else:
        reg_form=UserCreationForm()
    return render (request,"user/register.html",{'reg_form':reg_form})

