# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 18:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dentaire', '0009_auto_20170610_0133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.RenameField(
            model_name='rdv',
            old_name='id_rdv',
            new_name='id',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
