# Generated by Django 2.1.4 on 2019-01-08 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='phone',
        ),
    ]