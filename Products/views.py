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

def edit(request, id):  
    product = product.objects.get(id=id)  
    return render(request,'edit.html', {'product':product})  
def update(request, id):  
    product = product.objects.get(id=id)  
    form = product(request.POST, instance = product)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'product': product})  
def destroy(request, id):  
    product = product.objects.get(id=id)  
    product.delete()  
    return redirect("/show")