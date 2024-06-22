from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin
# Create your views here.

@xframe_options_sameorigin
def frameq9(request):
    temp=loader.get_template('q9.html')
    return HttpResponse(temp.render())
def displayq1(request):
    temp=loader.get_template('q1.html')
    return HttpResponse(temp.render())
def displayq2(request):
    temp=loader.get_template('q2.html')
    return HttpResponse(temp.render())
def displayq3(request):
    temp=loader.get_template('q3.html')
    return HttpResponse(temp.render())
def displayq4(request):
    temp=loader.get_template('q4.html')
    return HttpResponse(temp.render())
def displayhome(request):
    temp=loader.get_template('home.html')
    return HttpResponse(temp.render())
def displaygreen(request):
    temp=loader.get_template('green.html')
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
