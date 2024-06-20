from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def training(request):
	return HttpResponse("Python Training")

def akram(request):
	return HttpResponse("Hi Akram")
