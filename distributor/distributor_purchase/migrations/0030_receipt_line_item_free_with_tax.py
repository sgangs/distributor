# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-23 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor_purchase', '0029_receipt_line_item_quantity_returned'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt_line_item',
            name='free_with_tax',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
    ]
