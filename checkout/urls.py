from django.conf.urls import url
from .views import checkout
# simple url imported into main url
urlpatterns = [
    url(r'^$', checkout, name='checkout'),
]
