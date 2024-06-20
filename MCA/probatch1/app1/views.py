from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def displayhome(request):
    temp=loader.get_template('home.html')
    return HttpResponse(temp.render())

def q18(request):
    temp=loader.get_template('q18.html')
    return HttpResponse(temp.render())
def register(request):
    temp=loader.get_template('register.html')
    return HttpResponse(temp.render())

def fun1(request):
    temp="<h1> Hello world</h1>"
    return HttpResponse(temp)

def fun2(request):
    temp="<h1> Good Morning</h1>"
    return HttpResponse(temp)

def fun3(request):
    temp="<h1>Good Afternoon</h1>"
    return HttpResponse(temp)
