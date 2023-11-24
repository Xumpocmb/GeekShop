from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import Product, ProductCategory, Basket


def index(request):
    context = {
        'title': 'Geek Shop',
        'username': 'Geek',
    }
    return render(request, 'products/index.html', context=context)


def products(request, category_id=None, page=1):
    products = Product.objects.filter(category__id=category_id) if category_id else Product.objects.all()
    paginator = Paginator(products, 3)
    products_paginator = paginator.page(page)
    context = {
        'title': 'Geek Shop',
        'categories': ProductCategory.objects.all(),
        'products': products_paginator,
    }
    return render(request, 'products/products.html', context=context)


@login_required
def add_to_basket(request, product_id):
    # Add product to basket
    # 1. Get product from DB
    product = Product.objects.get(id=product_id)
    # 2. Add product to basket
    baskets = Basket.objects.filter(user=request.user, product=product)
    # 3. If basket is empty - create basket
    if not baskets.exists():
        # 4. Create basket
        Basket.objects.create(user=request.user, product=product, quantity=1)
    # 5. If basket exists - increase quantity
    else:
        # 6. Get basket
        basket = baskets.first()
        # 7. Increase quantity
        basket.quantity += 1
        # 8. Save basket
        basket.save()
    # 9. Redirect to basket
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_from_basket(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
