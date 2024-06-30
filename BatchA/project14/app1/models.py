from django.db import models

# Create your models here.
class Student(models.Model):
    fn=models.CharField(max_length=25)
    ln=models.CharField(max_length=20)
    course=models.CharField(max_length=20)

    def __str__(self):
        return self.fn
    
class Teacher(models.Model):
    fn=models.CharField(max_length=25)
    ln=models.CharField(max_length=20)
    sub=models.CharField(max_length=15)
    loc=models.CharField(max_length=15)
    sal=models.IntegerField()

    def __str__(self):
        return self.fn
