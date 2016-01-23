# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-21 02:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20160121_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingaddress',
            name='street',
            field=models.CharField(default='None', max_length=120),
        ),
        migrations.AlterField(
            model_name='product',
            name='dateadded',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 21, 2, 10, 53, 250883, tzinfo=utc)),
        ),
    ]
