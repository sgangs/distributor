# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-09 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retail_sales', '0007_invoice_line_item_product_hsn'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice_line_item',
            name='quantity_returned',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]