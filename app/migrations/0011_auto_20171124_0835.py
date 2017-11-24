# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-24 08:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20171123_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='time',
            field=models.TimeField(default=datetime.datetime(2017, 11, 24, 8, 35, 3, 473953, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='date',
            field=models.DateField(verbose_name=datetime.datetime(2017, 11, 24, 8, 35, 3, 473930, tzinfo=utc)),
        ),
    ]
