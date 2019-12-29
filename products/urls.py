# these urls will be linked to top level urls in ecommerce
from django.conf.urls import url, include
from .views import all_products

urlpatterns = [
    url(r'^$', all_products, name='products'),
]
