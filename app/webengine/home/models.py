from django.db import models


class Price(models.Model):
    scrap = models.CharField(max_length=150, db_index=True, verbose_name='металл')
    cost = models.FloatField(verbose_name='цена')
    created = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    class Meta:
        verbose_name = 'металл'
        verbose_name_plural = 'металлы'

    def __str__(self):
        return self.scrap
