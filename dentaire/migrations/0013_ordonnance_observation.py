# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-11 13:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentaire', '0012_auto_20170610_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordonnance',
            name='observation',
            field=models.CharField(default='null', max_length=254),
        ),
    ]
