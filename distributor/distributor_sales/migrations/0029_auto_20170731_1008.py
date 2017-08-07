# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-31 04:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor_sales', '0028_sales_invoice_is_final'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales_invoice',
            name='dl_1',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Drug License 1'),
        ),
        migrations.AddField(
            model_name='sales_invoice',
            name='dl_2',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Drug License 2'),
        ),
        migrations.AddField(
            model_name='sales_return',
            name='dl_1',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Drug License 1'),
        ),
        migrations.AddField(
            model_name='sales_return',
            name='dl_2',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Drug License 2'),
        ),
    ]
