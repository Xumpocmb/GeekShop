from django.urls import path

from products.views import ProductsListView, add_to_basket, remove_from_basket

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('category/<int:category_id>/', ProductsListView.as_view(), name='category'),
    path('page/<int:page>/', ProductsListView.as_view(), name='paginator'),
    path('add-to-basket/<int:product_id>/', add_to_basket, name='add_to_basket'),
    path('remove-from-basket/<int:basket_id>/', remove_from_basket, name='remove_from_basket'),
]
