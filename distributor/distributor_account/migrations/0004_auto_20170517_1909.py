# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-17 13:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor_account', '0003_auto_20170517_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]