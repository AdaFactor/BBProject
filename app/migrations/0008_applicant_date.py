# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-23 20:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_applicant'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 11, 23, 20, 21, 25, 865842)),
        ),
    ]
