# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-21 01:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20160121_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='dateadded',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 21, 1, 20, 17, 955593, tzinfo=utc)),
        ),
    ]
