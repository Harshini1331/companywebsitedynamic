from django.shortcuts import render
from .models import Product
from .models import People

# Create your views here.

def home(request):
    context = {}
    return render(request, 'companywebsite/home.html', context)

def products(request):
    context = {}

    context["products"] = Product.objects.all()

    return render(request, 'companywebsite/products.html', context)

def people(request):
    context = {}

    context["persons"] = People.objects.all()

    return render(request, 'companywebsite/people.html', context)

def contact(request):
    context = {}
    return render(request, 'companywebsite/contact.html', context)
