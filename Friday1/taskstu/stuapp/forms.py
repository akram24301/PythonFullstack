from django import forms
from .models import StudentModel


# creating a form
class StudentForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = StudentModel

		# specify fields to be used
		fields = [
			"fn",
			"ln",
			"course",
		]

		# fields ="__all__"	
