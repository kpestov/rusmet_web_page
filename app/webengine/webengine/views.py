from django.http import HttpResponse
from django.shortcuts import redirect


def redirect_home(request):
    return redirect('main_page_url', permanent=True)
