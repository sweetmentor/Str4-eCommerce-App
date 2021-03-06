"""chestergreen_elect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts import urls as accounts_urls
from django.conf.urls import url, include
from home import urls as home_urls
from product import urls as products_urls
from product import views
from cart import urls as carts_urls
from blogs import urls as blogs_urls
from review import urls as urls_reviews
from checkout import urls as checkout_urls
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_urls)),
    path('accounts/', include(accounts_urls)),
    path('cart/', include(carts_urls)),
    path('products/', include(products_urls)), 
    path('search/', views.do_search, name='search'),
    path('checkout/', include(checkout_urls)),
    path('reviews/', include(urls_reviews)),
    path('blogs/', include(blogs_urls)),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
]
