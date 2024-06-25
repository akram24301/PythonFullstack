from django.db import models

# Create your models here.
class Product(models.Model):
    productname = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=3)
    description = models.TextField()
    image = models.ImageField(upload_to='img') 


