# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-18 05:49
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('retail_sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retail_invoice',
            name='customer_gender',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='retail_invoice',
            name='customer_name',
            field=models.CharField(blank=True, db_index=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='retail_invoice',
            name='customer_phone_no',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, null=True),
        ),
    ]
