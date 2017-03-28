# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_eduadmin', '0028_auto_20170226_1724'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam',
            options={'ordering': ('year', 'term', 'serial_no')},
        ),
        migrations.AlterModelOptions(
            name='syllabus',
            options={'ordering': ('class_group', 'serial_no', 'id')},
        ),
        migrations.AddField(
            model_name='exam',
            name='serial_no',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='syllabus',
            name='serial_no',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='term',
            name='year',
            field=models.PositiveSmallIntegerField(db_index=True, default=2016, verbose_name='Academic Year'),
        ),
        migrations.AlterField(
            model_name='exam_creation',
            name='year',
            field=models.PositiveSmallIntegerField(db_index=True),
        ),
    ]