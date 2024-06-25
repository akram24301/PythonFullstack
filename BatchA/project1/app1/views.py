from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def home(request):
    temp="<h1>welcome to home </h1>"
    return HttpResponse(temp)