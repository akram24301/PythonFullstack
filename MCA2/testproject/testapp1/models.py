from django.db import models

# Create your models here.
class Member1(models.Model):
  firstname = models.CharField(max_length=25)
  lastname = models.CharField(max_length=25)