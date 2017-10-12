# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 21:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PickupLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_text', models.CharField(max_length=1000)),
                ('creation_date', models.DateTimeField(verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='PickupLineRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(verbose_name='date created')),
                ('vote', models.BooleanField()),
                ('pickup_line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapp.PickupLine')),
            ],
        ),
    ]
