# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-19 05:01
from __future__ import unicode_literals

from django.db import migrations, models
import places.validators


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20180719_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='location',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='popular_for',
            field=models.CharField(max_length=200, validators=[places.validators.validate_name]),
        ),
    ]
