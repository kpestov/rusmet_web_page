from django import forms
from .models import Price
from django.core.exceptions import ValidationError


class PriceForm(forms.Form):
    scrap = forms.CharField(max_length=150)
    cost = forms.FloatField()

    scrap.widget.attrs.update({'class': 'form-control'})
    cost.widget.attrs.update({'class': 'form-control'})

    def clean_scrap(self):
        new_scrap = self.cleaned_data['scrap'].upper()

        if Price.objects.filter(scrap__iexact=new_scrap).count():
            raise ValidationError('Название лома должно быть уникальным! У вас уже имеется "{}"'.format(new_scrap))
        return new_scrap

    def save(self):
        new_price = Price.objects.create(
            scrap=self.cleaned_data['scrap'],
            cost=self.cleaned_data['cost']
        )
        return new_price
