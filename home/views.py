from django.shortcuts import render, get_object_or_404 
from product.models import Product
# Create your views here.
def get_index(request):
    products = Product.objects.all()
    return render(request, 'home/index.html', {'products': products})