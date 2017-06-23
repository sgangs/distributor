# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-01 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor_sales', '0007_auto_20170601_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice_line_item',
            name='discount2_type',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='invoice_line_item',
            name='discount2_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]