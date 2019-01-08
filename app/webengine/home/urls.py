from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', HomePage.as_view(), name='main_page_url'),
    path('price/create/', PriceCreate.as_view(), name='price_create_url'),
    path('price/update/<str:scrap>/', PriceUpdate.as_view(), name='price_update_url'),
    path('price/delete/<str:scrap>/', PriceDelete.as_view(), name='price_delete_url')
]