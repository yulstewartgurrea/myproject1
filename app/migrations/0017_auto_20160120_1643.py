# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-20 16:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20160120_1439'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billingaddress',
            old_name='country',
            new_name='brgy',
        ),
        migrations.RenameField(
            model_name='permanentaddress',
            old_name='country',
            new_name='brgy',
        ),
        migrations.AlterField(
            model_name='product',
            name='dateadded',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 20, 16, 43, 26, 298972, tzinfo=utc)),
        ),
    ]
