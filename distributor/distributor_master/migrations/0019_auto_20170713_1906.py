# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-13 13:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor_master', '0018_auto_20170705_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tax_structure',
            name='percentage',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
