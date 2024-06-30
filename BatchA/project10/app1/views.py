from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Teacher

# Create your views here.
def display_teacher(request):
    allteach = Teacher.objects.all().values()
    temp = loader.get_template('all_teacher.html')
    context={
        'allteach' : allteach,
    }
    return HttpResponse(temp.render(context,request))