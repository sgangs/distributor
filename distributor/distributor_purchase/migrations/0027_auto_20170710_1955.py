# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-10 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor_purchase', '0026_auto_20170710_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipt_line_item',
            name='free_with_tax',
        ),
        migrations.RemoveField(
            model_name='receipt_line_item',
            name='free_without_tax',
        ),
        migrations.AlterField(
            model_name='receipt_line_item',
            name='mrp',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='MRP'),
        ),
        migrations.AlterField(
            model_name='receipt_line_item',
            name='purchase_price',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='receipt_line_item',
            name='tentative_sales_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]