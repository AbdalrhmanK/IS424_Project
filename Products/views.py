from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from .models import product
from .forms import productForm
# Create your views here.

def add(request):
    if request.method == 'POST':
        form = productForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home"))  # Replace 'show' with the appropriate URL name
    else:
     form = productForm()
     return render(request, 'Products/add.html', {'form': form})

def home(request):
    prod = product.objects.all()
    return render(request , 'Products/homePage.html' ,{"products" : prod})

def view(request, product_id):  
     products = product.objects.get(id=product_id)  
     return render(request,'Products/view.html', {'product':products})  
    
    
def edit(request, product_id):  
     products = product.objects.get(id=product_id)  
     return render(request,'Products/edit.html', {'product':products})  
  
    
def update(request,product_id):  
    if request.method == 'POST':
     products = product.objects.get(id=product_id)  
     form = productForm(request.POST,instance=products)  
     print(form)
     print(products)
     if form.is_valid():  
        form.save()  
        return HttpResponseRedirect(reverse("home"))
    return render(request, 'Products/edit.html', {'product':products})      