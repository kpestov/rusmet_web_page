from django.urls import path
from .views import *


urlpatterns = [
    path('', render_home_page, name='main_page_url')
]