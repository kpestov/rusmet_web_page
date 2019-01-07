from django.db import models


class Price(models.Model):
    scrap = models.CharField(max_length=150, db_index=True)
    cost = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'kind of metall:{}, date creation:{}, date update:{}'.format(self.scrap, self.created, self.updated)



