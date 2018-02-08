# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-23 04:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor_sales', '0039_auto_20180123_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales_return',
            name='return_id',
            field=models.BigIntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name='sales_return',
            name='return_type',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]