from django.shortcuts import render, redirect


class OblectCreateMixin:
    super_model = None
    model = None
    model_form = None
    template = None

    def get(self, request):
        form = self.model_form
        prices = self.model.objects.all()
        last_updated_date = self.super_model.get_last_updated_date()
        return render(request, self.template, context={'form': form, 'prices': prices,
                                                                  'last_date': last_updated_date})

    def post(self, request):
        bound_form = self.model_form(request.POST)

        if bound_form.is_valid():
            bound_form.save()
            return redirect('price_create_url')
        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, scrap):
        obj = self.model.objects.get(scrap__iexact=scrap)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, scrap):
        obj = self.model.objects.get(scrap__iexact=scrap)
        bound_form = self.model_form(request.POST, instance=obj)

        if bound_form.is_valid():
            bound_form.save()
            return redirect('price_create_url')
        return render(request, self.template, context={'form': bound_form})


class ObjectDeleteMixin:
    model = None
    template = None

    def get(self, request, scrap):
        obj = self.model.objects.get(scrap__iexact=scrap)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

    def post(self, request, scrap):
        obj = self.model.objects.get(scrap__iexact=scrap)
        obj.delete()
        return redirect('price_create_url')