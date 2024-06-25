from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Student

# Create your views here.
def home(request):
    temp=loader.get_template('home.html')
    return HttpResponse(temp.render())
def display_cr(request):
    temp=loader.get_template('cr.html')
    return HttpResponse(temp.render())

def display_student(request):
    allstu = Student.objects.all().values()
    temp = loader.get_template('all_student.html')
    context={
        'allstu' : allstu,
    }
    return HttpResponse(temp.render(context,request))