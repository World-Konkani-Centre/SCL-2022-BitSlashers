# Generated by Django 4.0.6 on 2022-07-28 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeGroW', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='otp',
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='pincode',
            field=models.CharField(default=111111, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(default=121, max_length=20),
            preserve_default=False,
        ),
    ]