# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-23 09:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20160123_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='dateadded',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 23, 9, 13, 16, 50946, tzinfo=utc)),
        ),
    ]
