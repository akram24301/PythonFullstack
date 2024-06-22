from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun101(request):
    return HttpResponse('welcome to home page fun101 of testapp1 called')
def fun102(request):
    return HttpResponse('fun102 of testapp1 called')
def fun103(request):
    return HttpResponse('fun103 of testapp1 called')