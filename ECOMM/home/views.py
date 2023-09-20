from django.shortcuts import render
from products.models import Product

def index(request):
   # return render(request, 'home/index.html')
   context={'products':Product.objects.all()}
   return render(request, 'home/index.html', context)