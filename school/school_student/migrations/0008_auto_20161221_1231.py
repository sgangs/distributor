# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-21 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_student', '0007_student_school_student_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='school_student_id',
        ),
        migrations.AlterField(
            model_name='student',
            name='local_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='School student ID'),
        ),
    ]
