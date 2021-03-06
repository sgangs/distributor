# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 09:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_salary', '0007_auto_20170225_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadre_default_salary',
            name='edliEmployer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cadreDefaultSalary_edliEmployer', to='school_salary.edli_employer'),
        ),
        migrations.AddField(
            model_name='staff_salary_definition',
            name='edliEmployer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staffSalary_edliEmployer', to='school_salary.edli_employer'),
        ),
    ]
