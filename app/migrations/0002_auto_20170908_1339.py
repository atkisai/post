# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 10:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='musician',
            old_name='first_name',
            new_name='first',
        ),
        migrations.RenameField(
            model_name='musician',
            old_name='last_name',
            new_name='last',
        ),
    ]