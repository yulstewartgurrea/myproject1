# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-17 06:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='dateadded',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 17, 6, 19, 14, 777049, tzinfo=utc)),
        ),
    ]