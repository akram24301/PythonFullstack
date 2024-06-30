from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Student

# Create your views here.
def student_entry(request):
    return render(request,'student_entry.html')

def process_student_entry(request):
    if request.method == 'POST':
        fn_inp =request.POST.get('fn')
        ln_inp =request.POST.get('ln')
        course_inp=request.POST.get('course')
        ob=Student(fn=fn_inp,ln=ln_inp,course=course_inp)
        ob.save()
        return HttpResponse("Data sucessfully inserted")
    else:
        return HttpResponse("Invalid request method")

def display_student(request):
    allstu = Student.objects.all().values()
    temp = loader.get_template('all_student.html')
    context={
        'allstu' : allstu,
    }
    return HttpResponse(temp.render(context,request))

def home(request):
    temp=loader.get_template('home.html')
    return HttpResponse(temp.render())
def display_cr(request):
    temp=loader.get_template('cr.html')
    return HttpResponse(temp.render())


    
