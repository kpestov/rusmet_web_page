import datetime
from django.shortcuts import render
from .models import Price


def render_home_page(request):
    prices = Price.objects.all()

    time = Price.objects.all()
    timestamps = ['{}.{}.{}'.format(ts.updated.day, ts.updated.month, ts.updated.year) for ts in time]
    last_updated_date = sorted(timestamps, key=lambda x: datetime.datetime.strptime(x, '%d.%m.%Y'), reverse=True)[0]

    return render(request, 'home/index.html', context={'prices': prices, 'last_date': last_updated_date})


#def get_last_updated_date(request):
#    time = Price.objects.all()
#    timestamps = ['{}.{}.{}'.format(ts.updated.day, ts.updated.month, ts.updated.year) for ts in time]
#    last_updated_date = sorted(timestamps, key=lambda d: tuple(map(int, d.split('.'))))[0]
#    return render(request, 'home/index.html', context={'last_date': last_updated_date})



