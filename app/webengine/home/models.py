from django.db import models
from django.urls import reverse


class Price(models.Model):
    scrap = models.CharField(max_length=150, db_index=True)
    cost = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_update_url(self):
        return reverse('price_update_url', kwargs={'scrap': self.scrap})

    def get_delete_url(self):
        return reverse('price_delete_url', kwargs={'scrap': self.scrap})


    def __str__(self):
        return 'kind of metall:{}, date creation:{}, date update:{}'.format(self.scrap, self.created, self.updated)



