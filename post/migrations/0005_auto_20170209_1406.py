# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20170201_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='dateshow',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='timeshow',
            field=models.TimeField(),
        ),
    ]