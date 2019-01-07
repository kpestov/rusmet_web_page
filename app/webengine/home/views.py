import datetime
from django.views.generic import View
from django.shortcuts import render, redirect
from .models import Price
from .forms import PriceForm


class HomePage(View):
    def get_last_updated_date(self):
        time = Price.objects.all()
        timestamps = ['{}.{}.{}'.format(ts.updated.day, ts.updated.month, ts.updated.year) for ts in time]
        last_updated_date = sorted(timestamps, key=lambda x: datetime.datetime.strptime(x, '%d.%m.%Y'), reverse=True)[0]
        return last_updated_date

    def get(self, request):
        prices = Price.objects.all()
        last_updated_date = self.get_last_updated_date()
        return render(request, 'home/index.html', context={'prices': prices, 'last_date': last_updated_date})


class PriceCreate(View):
    def get(self, request):
        form = PriceForm()
        prices = Price.objects.all()
        last_updated_date = HomePage().get_last_updated_date()
        return render(request, 'home/price_create.html', context={'form': form, 'prices': prices,
                                                                  'last_date': last_updated_date})

    def post(self, request):
        bound_form = PriceForm(request.POST)

        if bound_form.is_valid():
            bound_form.save()
            return redirect('price_create_url')
        return render(request, 'home/price_create.html', context={'form': bound_form})



