# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_salary', '0010_auto_20170304_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic_salary_rule',
            name='salary_cycle_end',
            field=models.CharField(max_length=4),
        ),
    ]
