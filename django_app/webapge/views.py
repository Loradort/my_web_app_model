from django.shortcuts import render, HttpResponse
from . import models
# Create your views here.

def home(request):
    context = {}

    students = models.student.objects.all().order_by("-id")
    for student in students :
        student . prefix_str = getmodelschoice(
            student.prefix, models.prefix_choices
        )
    context = {
        'students' : students,
    }
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def studentdetails(request, id) :
    context = {}
    # student = models.student.objects.get(id=id)
    students = models.student.objects.filter(id=id)
    for student in students :
        student . prefix_str = getmodelschoice(
            student.prefix, models.prefix_choices
        )
        context['student'] = student
    return render (request, 'details.html', context)

def getmodelschoice(num, choices):
    for choice in choices:
        if choice[0] == num:
            return choice [1]