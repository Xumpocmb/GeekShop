from django.shortcuts import render
from .models import Product, ProductCategory


def index(request):
    context = {
        'title': 'Geek Shop',
        'username': 'Geek',
    }
    return render(request, 'products/index.html', context=context)


def products(request):
    context = {
        'title': 'Geek Shop',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'products/products.html', context=context)
