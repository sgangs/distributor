# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-12 04:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_eduadmin', '0014_remove_subject_teacher_key'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classstudent',
            options={'ordering': ('roll_no',)},
        ),
        migrations.RemoveField(
            model_name='classstudent',
            name='slug',
        ),
    ]