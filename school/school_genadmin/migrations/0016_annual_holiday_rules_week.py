# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-28 08:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_genadmin', '0015_auto_20170128_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='annual_holiday_rules',
            name='week',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
