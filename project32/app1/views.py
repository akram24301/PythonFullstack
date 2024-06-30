from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ProductForm
from .models import Product

# Create your views here.
def index(request):
    products=Product.objects.all()
    context={
        'products':products
    }
    return render(request,'index.html',context)

def upload_image(request):
    if request.method=='POST':
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect(index)
    else:
        form=ProductForm()
        context= {
            'form':form
        }

    return render(request,'upload_image.html',context)


