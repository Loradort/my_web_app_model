from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')
    # return HttpResponse("This is my django website")

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')