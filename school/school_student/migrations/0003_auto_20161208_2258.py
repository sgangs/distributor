# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-08 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_student', '0002_remove_student_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='local_id',
            field=models.CharField(blank=True, max_length=50, verbose_name='Please fill this if you have some other student ID'),
        ),
        migrations.AddField(
            model_name='student_guardian',
            name='profession',
            field=models.TextField(blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='student_education',
            unique_together=set([('student', 'degree_name')]),
        ),
        migrations.AlterUniqueTogether(
            name='student_guardian',
            unique_together=set([('student', 'relation', 'tenant')]),
        ),
    ]
