# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-01 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor_purchase', '0008_auto_20170601_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase_payment',
            name='final_payment_delay',
        ),
        migrations.AlterField(
            model_name='purchase_payment',
            name='paid_on',
            field=models.DateField(blank=True, db_index=True, null=True),
        ),
    ]
