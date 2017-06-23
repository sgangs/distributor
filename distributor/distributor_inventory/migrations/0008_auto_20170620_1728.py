# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-20 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor_inventory', '0007_auto_20170619_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory_ledger',
            name='transaction_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Purchase'), (2, 'Sales'), (3, 'Sales Return'), (4, 'Other Inward'), (5, 'Purchase Return'), (6, 'Other Outward'), (7, 'Transfer Outward'), (8, 'Transfer Inward'), (9, 'Retail Sales'), (9, 'Retail Sales Return')], db_index=True, verbose_name='Transaction type'),
        ),
    ]
