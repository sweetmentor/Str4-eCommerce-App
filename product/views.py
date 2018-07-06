from django.shortcuts import render, HttpResponse, get_object_or_404 
from .models import Product
from review.forms import ReviewForm

# Create your views here.

def get_products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {"products": products})


def product_detail(request, id):
    
    product = get_object_or_404(Product, id=id)
    form = ReviewForm()
    return render(request, "products/productdetail.html", {"product": product, 'review_form': form })
 
 
    
def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['query'])
    return render(request, "products/products.html", {"products": products})