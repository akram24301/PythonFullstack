from django.urls import path
from . import views

urlpatterns=[
    path('home/',views.home,name='home'),
    path('display_cr/',views.display_cr,name='display_cr'),
    path('display_student/',views.display_student,name='display_student'),
    path('student_entry/',views.student_entry,name='student_entry'),
    path('process_student_entry/',views.process_student_entry,name='process_student_entry'),
    ]