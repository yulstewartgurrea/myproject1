# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-20 12:50
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20160120_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billingaddress',
            name='acct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='permanentaddress',
            name='acct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='dateadded',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 20, 12, 50, 0, 449435, tzinfo=utc)),
        ),
    ]