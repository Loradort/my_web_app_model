from django.shortcuts import render, HttpResponse
from . import models
# Create your views here.

def home(request):
    context = {}
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def studnetDetails():
    return