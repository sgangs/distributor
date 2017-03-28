# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 07:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_eduadmin', '0043_auto_20170327_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='syllabus',
            name='term',
        ),
        migrations.AlterField(
            model_name='syllabus_topic',
            name='syllabus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='syllabusTopic_syllabusSubject', to='school_eduadmin.Syllabus'),
        ),
    ]