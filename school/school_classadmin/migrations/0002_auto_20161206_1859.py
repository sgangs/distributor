# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-06 13:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school_classadmin', '0001_initial'),
        ('school_eduadmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam_report',
            name='class_section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examReport_classadmin_eduadmin_classSection', to='school_eduadmin.class_section'),
        ),
        migrations.AddField(
            model_name='exam_report',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examReport_classadmin_eduadmin_exam', to='school_eduadmin.Exam'),
        ),
    ]
