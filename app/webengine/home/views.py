import datetime
from django.shortcuts import render
from django.views.generic import View
from .models import Price


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
