from django import forms
from .models import Price, FeedBack
from django.core.exceptions import ValidationError


class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        fields = ['scrap', 'cost']

        widgets = {
            'scrap': forms.TextInput(attrs={'class': 'form-control'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'})
        }

    def clean_scrap(self):
        new_scrap = self.cleaned_data['scrap'].upper()

        # if Price.objects.filter(scrap__iexact=new_scrap).count():
        #     raise ValidationError('Название лома должно быть уникальным! У вас уже имеется "{}"'.format(new_scrap))
        return new_scrap


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ['customer_name', 'email', 'message']

        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя...', 'name': 'name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail...', 'name': 'email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Сообщение...', 'name': 'text'}),
        }

