import datetime
from django.views.generic import View
from .models import Price
from .forms import PriceForm
from .utils import *

from django.contrib.auth.mixins import LoginRequiredMixin


class HomePage(View):
    def get_last_updated_date(self):
        time = Price.objects.all()
        try:
            timestamps = ['{}.{}.{}'.format(ts.updated.day, ts.updated.month, ts.updated.year) for ts in time]
            last_updated_date = sorted(timestamps, key=lambda x: datetime.datetime.strptime(x, '%d.%m.%Y'), reverse=True)[0]
        except Exception:
            last_updated_date = ''
            return last_updated_date
        return last_updated_date

    def get(self, request):
        prices = Price.objects.all()
        last_updated_date = self.get_last_updated_date()
        return render(request, 'home/index.html', context={'prices': prices, 'last_date': last_updated_date})


class PriceCreate(LoginRequiredMixin, OblectCreateMixin, View):
    super_model = HomePage()
    model = Price
    model_form = PriceForm
    template = 'home/price_create.html'
    raise_exception = True


class PriceUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Price
    model_form = PriceForm
    template = 'home/price_update.html'
    raise_exception = True


class PriceDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Price
    template = 'home/price_delete.html'
    raise_exception = True


# class PriceDelete(View):
#     def get(self, request, scrap):
#         price = Price.objects.get(scrap__iexact=scrap)
#         return render(request, 'home/price_delete.html', context={'price': price})
#
#     def post(self, request, scrap):
#         price = Price.objects.get(scrap__iexact=scrap)
#         price.delete()
#         return redirect('price_create_url')










