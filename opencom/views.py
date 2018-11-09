# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from . forms import ImageUploadForm
from django.conf import settings
# Create your views here.
def index(request):
 
   return render(request,'open/test.html')

 


def dface(request):
  if request.method == 'POST':
     form = ImageUploadForm(request.POST, request.FILES)
     if form.is_valid():
        post = form.save(commit=False)
        post.save()
 
        imageURL = settings.MEDIA_URL + form.instance.document.name
        #opencv_dface(settings.MEDIA_ROOT_URL + imageURL)
 
        return render(request, 'opencv_webapp/dface.html', {'form':form, 'post':post})
  else:
     form = ImageUploadForm()
  return render(request, 'dface.html',{'form':form})

