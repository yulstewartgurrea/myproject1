# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-20 05:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20160120_0342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img1', models.FileField(upload_to=None)),
                ('img2', models.FileField(upload_to=None)),
                ('img3', models.FileField(upload_to=None)),
                ('img4', models.FileField(upload_to=None)),
                ('img5', models.FileField(upload_to=None)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='dateadded',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 20, 5, 14, 9, 357195, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='image',
            name='pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product'),
        ),
    ]
