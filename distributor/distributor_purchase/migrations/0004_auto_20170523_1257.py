# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-23 07:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor_purchase', '0003_auto_20170517_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipt_line_item',
            name='tax',
        ),
        migrations.AddField(
            model_name='receipt_line_item',
            name='tax_percent',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
