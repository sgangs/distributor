# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-11 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor_sales', '0029_auto_20170731_1008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales_payment',
            name='final_payment_delay',
        ),
        migrations.AlterField(
            model_name='sales_payment',
            name='cheque_rtgs_number',
            field=models.CharField(blank=True, db_index=True, max_length=30, null=True),
        ),
    ]
