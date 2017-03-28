# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 17:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_teacher', '0014_auto_20170304_1349'),
        ('school_hr', '0012_auto_20170311_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher_attendance',
            name='slug',
        ),
        migrations.AlterUniqueTogether(
            name='staff_cadre_linking',
            unique_together=set([('cadre', 'teacher', 'year')]),
        ),
    ]