# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-17 14:32
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160117_0722'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAdress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postalcode', models.CharField(max_length=120)),
                ('country', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('pnum', models.CharField(max_length=120)),
                ('is_active', models.BooleanField(default=True)),
                ('acct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PermanentAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postalcode', models.CharField(max_length=120)),
                ('country', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('pnum', models.CharField(max_length=120)),
                ('is_active', models.BooleanField(default=True)),
                ('acct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PriceRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=120)),
                ('lname', models.CharField(max_length=120)),
                ('is_active', models.BooleanField(default=True)),
                ('acct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='dateadded',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 17, 14, 32, 45, 356317, tzinfo=utc)),
        ),
    ]
