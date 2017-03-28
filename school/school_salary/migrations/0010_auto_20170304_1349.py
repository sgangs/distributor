# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 08:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_account', '0020_auto_20170223_2009'),
        ('school_salary', '0009_auto_20170227_0102'),
    ]

    operations = [
        migrations.CreateModel(
            name='basic_salary_rule',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('working_days', models.PositiveSmallIntegerField(verbose_name='Number of working days in month')),
                ('salary_cycle_start', models.PositiveSmallIntegerField()),
                ('salary_cycle_end', models.PositiveSmallIntegerField()),
                ('salary_cycle_payment', models.PositiveSmallIntegerField()),
                ('employer_contribution_expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basicSalaryRule_salary_account_account', to='school_account.Account')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basicSalaryStructure_salary_user_tenant', to='school_user.Tenant')),
            ],
        ),
        migrations.RemoveField(
            model_name='basic_salary_structure',
            name='tenant',
        ),
        migrations.DeleteModel(
            name='basic_salary_structure',
        ),
    ]