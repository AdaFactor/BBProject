# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-23 20:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20171123_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='date',
            field=models.DateField(verbose_name=datetime.datetime(2017, 11, 23, 20, 25, 43, 793967, tzinfo=utc)),
        ),
    ]
