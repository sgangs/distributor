# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_student', '0018_auto_20170221_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='key',
            field=models.CharField(db_index=True, max_length=64),
        ),
    ]
