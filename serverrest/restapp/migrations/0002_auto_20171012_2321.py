# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 21:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pickupline',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='pickuplinerating',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='date created'),
        ),
    ]