# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-07-13 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('vehicle', models.CharField(max_length=50)),
                ('capcity', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('price', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]
