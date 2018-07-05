from django.urls import path
from product.views import get_products, do_search, product_detail


urlpatterns = [
    path('products/', get_products, name='products'),
    path('search/', do_search, name='search'),
    path('<int:id>/', product_detail, name='product_detail'),
   
]