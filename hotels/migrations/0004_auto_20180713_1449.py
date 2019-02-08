# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-13 14:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_hotel_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotel',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
