# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_hr', '0007_staff_cadre_linking_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_cadre_linking',
            name='cadre_type',
            field=models.CharField(db_index=True, default='Teacher', max_length=10),
        ),
    ]