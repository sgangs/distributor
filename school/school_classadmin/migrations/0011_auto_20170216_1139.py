# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-16 06:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_classadmin', '0010_auto_20170103_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='slug',
        ),
        # migrations.RemoveField(
        #     model_name='exam_report',
        #     name='examiner',
        # ),
        migrations.RemoveField(
            model_name='exam_report',
            name='external_score',
        ),
        migrations.RemoveField(
            model_name='exam_report',
            name='internal_score',
        ),
        migrations.RemoveField(
            model_name='exam_report',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='homework',
            name='slug',
        ),
    ]
