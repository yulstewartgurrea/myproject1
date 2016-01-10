# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-10 05:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.manager
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20160104_0500'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['cname']},
        ),
        migrations.AlterModelOptions(
            name='myuser',
            options={'ordering': ['email']},
        ),
        migrations.AlterModelManagers(
            name='category',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='dateadded',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 5, 45, 55, 154830, tzinfo=utc)),
        ),
    ]