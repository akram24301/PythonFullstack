from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    #specify the name of the model to use
    class Meta:
        model=Student
        fields="__all__"