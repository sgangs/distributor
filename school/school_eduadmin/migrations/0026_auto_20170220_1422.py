# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_eduadmin', '0025_auto_20170219_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='period_from',
            field=models.DateField(default='2016-01-01', verbose_name='Exam Class Starts'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exam',
            name='period_to',
            field=models.DateField(default='2017-01-01', verbose_name='Exam Class Ends'),
            preserve_default=False,
        ),
        # migrations.AlterField(
        #     model_name='exam',
        #     name='year',
        #     field=models.PositiveSmallIntegerField(db_index=True, default=2016),
        #     preserve_default=False,
        # ),
    ]