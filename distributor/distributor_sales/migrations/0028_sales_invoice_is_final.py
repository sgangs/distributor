# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-28 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor_sales', '0027_remove_sales_invoice_is_b2b_registered'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales_invoice',
            name='is_final',
            field=models.BooleanField(default=True),
        ),
    ]
