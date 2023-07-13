from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is my django website")

def about(request):
    return HttpResponse("About me")

def contact(request):
    return HttpResponse("Contact me")