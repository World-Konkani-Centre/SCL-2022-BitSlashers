# Generated by Django 4.0.6 on 2022-08-10 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WeGroW', '0004_rename_country_product_seller_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]