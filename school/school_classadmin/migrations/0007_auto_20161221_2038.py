# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-21 15:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_eduadmin', '0007_auto_20161221_2038'),
        ('school_classadmin', '0006_auto_20161217_0924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam_report',
            name='examInvigilator',
        ),
        migrations.AddField(
            model_name='attendance',
            name='remarks',
            field=models.TextField(default='a'),
            preserve_default=False,
        ),
        # migrations.AddField(
        #     model_name='exam_report',
        #     name='examiner',
        #     field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='examReport_classadmin_eduadmin_examiner', to='school_eduadmin.Examiner'),
        #     preserve_default=False,
        # ),
    ]
