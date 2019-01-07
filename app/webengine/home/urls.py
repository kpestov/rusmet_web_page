from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePage.as_view(), name='main_page_url'),
    path('price/create', PriceCreate.as_view(), name='price_create_url')
]