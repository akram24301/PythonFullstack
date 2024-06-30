from django import forms
from .models import Student
from .models import Teacher

class StudentForm(forms.ModelForm):
    #specify the name of the model to use
    class Meta:
        model=Student
        fields=["fn","course"]

class TeacherForm(forms.ModelForm):
    #specify the name of the model to use
    class Meta:
        model=Teacher
        fields="__all__"