# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-23 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor_purchase', '0044_auto_20180321_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_line_item',
            name='product_sku',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='receipt_line_item',
            name='product_sku',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='return_line_item',
            name='product_sku',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
