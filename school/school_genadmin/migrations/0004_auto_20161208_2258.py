# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-08 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_genadmin', '0003_auto_20161208_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='name',
            field=models.CharField(db_index=True, max_length=20),
        ),
    ]
