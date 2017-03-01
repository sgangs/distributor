# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-15 04:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_teacher', '0010_auto_20170204_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='staff_type',
            field=models.CharField(choices=[('Teacher', 'Teacher'), ('Admin', 'Admin'), ('Principal', 'Principal'), ('Accounts', 'Accounts'), ('Collector', 'Fee Collector')], default='T', max_length=2),
        ),
    ]
