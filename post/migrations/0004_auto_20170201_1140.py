# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 11:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20170125_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dateshow',
            field=models.DateField(default=datetime.date(2017, 2, 1)),
        ),
        migrations.AlterField(
            model_name='post',
            name='timeshow',
            field=models.TimeField(default=datetime.time(11, 40, 17, 659188)),
        ),
    ]
