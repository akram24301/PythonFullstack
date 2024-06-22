from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun201(request):
    return HttpResponse('fun201 of testapp1 called')
def fun202(request):
    return HttpResponse('fun202 of testapp1 called')
def fun203(request):
    return HttpResponse('fun203 of testapp1 called')