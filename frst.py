from django.db import models 
from django.contrib.auth.models import User
import uuid

class BaseModel(models.Model):
    uid=models.UUIDField(defualt=uuid.uuid4,editable=False,primary_key=True)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now_add=True)
    class Meta:
        abstract=True

class DairyCategory(BaseModel):
    category_name=models.CharField(max_length=100)

class Product(BaseModel):
    category=models.ForeignKey(DairyCategory,on_delete=models.CASCADE,related_name="pizzas")  
    Product_name=models.CharField(max_length=100)
    price=models.IntegerField(default=100)
    images=models.ImageField(upload_to='photos/') 

class Cart(BaseModel):
    user=models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL,related_name="carts")
    is_paid=models.BooleanField(default=False)
    
class DairyItems(BaseModel):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="cart_item")
    product=models.ForeignKey(Product,on_delete=models.CASADE)
