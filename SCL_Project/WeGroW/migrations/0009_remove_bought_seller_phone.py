# Generated by Django 4.0.6 on 2022-08-14 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WeGroW', '0008_sold_forsale_bought'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bought',
            name='seller_phone',
        ),
    ]
