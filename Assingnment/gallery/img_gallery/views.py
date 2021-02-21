from django.shortcuts import render, redirect
from .models import Photo
from .forms import PhotoForm
from django.contrib import messages

# Create your views here.

def gallery(request):
    if request.method=="POST":
        photo_form=PhotoForm(request.POST, request.FILES)
        if photo_form.is_valid():
            photo_form.save()
            messages.success(request,f'Photo Uploaded Successfully')
            return redirect ("gallery")

    else:
        photo_form=PhotoForm()
    img = Photo.objects.all()
    return render (request,"img_gallery/galery.html",{'img':img,'photo_form':photo_form})

