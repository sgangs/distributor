# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-28 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_invoice',
            name='invoice_id',
            field=models.CharField(max_length=12),
        ),
    ]
