# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-04 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distribution_master', '0003_auto_20160904_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_no',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='phone_no',
            field=models.TextField(blank=True),
        ),
    ]
