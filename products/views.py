from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from products.models import Product, ProductCategory, Basket
from common.views import TitleMixin


class IndexView(TitleMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Geek Shop - Главная'


class ProductsListView(TitleMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3
    title = 'Geek Shop'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        if category_id:
            queryset = queryset.filter(category__id=category_id)
        return queryset


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
