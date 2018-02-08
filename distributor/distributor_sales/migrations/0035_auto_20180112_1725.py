# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-12 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor_sales', '0034_auto_20171224_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='return_line_item',
            name='tax_percent',
        ),
        migrations.RemoveField(
            model_name='return_line_item',
            name='vat_type',
        ),
        migrations.AddField(
            model_name='sales_invoice',
            name='total_purchase_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='sales_return',
            name='total_purchase_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]