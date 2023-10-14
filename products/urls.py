from django.urls import path

from products.views import products, add_to_basket, remove_from_basket

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('add-to-basket/<int:product_id>/', add_to_basket, name='add_to_basket'),
    path('remove-from-basket/<int:basket_id>/', remove_from_basket, name='remove_from_basket'),
]
