# Generated by Django 3.0.6 on 2020-06-27 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='cost',
            field=models.CharField(max_length=150, verbose_name='цена'),
        ),
    ]
