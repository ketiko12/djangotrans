from django.urls import path
from home.views import index
from products.views import get_products

urlpatterns=[
    #path('', index, name='index'),
    path('<slug>', get_products, name='get_product')
]