from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    temp=loader.get_template('home.html')
    return HttpResponse(temp.render())
def display_cr(request):
    temp=loader.get_template('cr.html')
    return HttpResponse(temp.render())