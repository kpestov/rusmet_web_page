import datetime
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.views.generic import View
from .models import Price
from .forms import PriceForm, FeedbackForm
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
        feedback_form = FeedbackForm()
        prices = Price.objects.all()
        last_updated_date = self.get_last_updated_date()
        return render(request, 'home/index.html', context={'prices': prices, 'last_date': last_updated_date,
                                                           'feedback_form': feedback_form})

    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            customer_name = form.cleaned_data['customer_name']
            sender = form.cleaned_data['email']
            subject = 'Site contact form'
            form_message = form.cleaned_data['message']
            recepients = ['kpestov91@gmail.com']

            contact_message = '{} {} {}'.format(customer_name, sender, form_message)

            try:
                send_mail(
                          subject,
                          contact_message,
                          'kpestov91@gmail.com',
                          recepients
                          )

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('main_page_url')


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










