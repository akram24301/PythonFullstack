# import the standard Django Model
# from built-in library
from django.db import models

# declare a new model with a name "GeeksModel"
class StudentModel(models.Model):

	# fields of the model
	fn= models.CharField(max_length = 200)
	ln = models.CharField(max_length = 200)
	course= models.CharField(max_length = 200)

	# renames the instances of the model
	# with their title name
	def __str__(self):
		return self.fn

