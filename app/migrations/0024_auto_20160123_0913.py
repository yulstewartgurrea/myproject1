# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-23 09:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20160121_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img1',
            field=models.FileField(upload_to='pimages'),
        ),
        migrations.AlterField(
            model_name='image',
            name='img2',
            field=models.FileField(upload_to='pimages'),
        ),
        migrations.AlterField(
            model_name='image',
            name='img3',
            field=models.FileField(upload_to='pimages'),
        ),
        migrations.AlterField(
            model_name='image',
            name='img4',
            field=models.FileField(upload_to='None'),
        ),
        migrations.AlterField(
            model_name='image',
            name='img5',
            field=models.FileField(upload_to='None'),
        ),
        migrations.AlterField(
            model_name='product',
            name='dateadded',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 23, 9, 13, 8, 376532, tzinfo=utc)),
        ),
    ]
