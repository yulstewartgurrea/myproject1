# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-10 07:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20160110_0546'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='category',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='cid',
        ),
        migrations.AddField(
            model_name='product',
            name='cid',
            field=models.ManyToManyField(to='app.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='dateadded',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 7, 32, 32, 714006, tzinfo=utc)),
        ),
    ]
