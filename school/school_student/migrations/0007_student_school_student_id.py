# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-18 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_student', '0006_student_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='school_student_id',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
