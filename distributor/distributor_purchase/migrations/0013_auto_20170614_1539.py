# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-14 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor_purchase', '0012_auto_20170613_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='debit_note',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='debit_note_line_item',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='purchase_payment',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='purchase_receipt',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='receipt_line_item',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]