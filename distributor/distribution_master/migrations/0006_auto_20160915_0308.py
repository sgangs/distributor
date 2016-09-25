# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-15 03:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('distribution_user', '0001_initial'),
        ('distribution_master', '0005_auto_20160904_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='accountChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('remarks', models.TextField(blank=True)),
                ('account_type', models.CharField(choices=[('Assets', 'Assets'), ('Liabilities', 'Liabilities'), ('Equity', 'Equity'), ('Revenue', 'Revenue'), ('Expense', 'Expense')], max_length=12, verbose_name='Account type')),
                ('slug', models.SlugField(max_length=20)),
                ('key', models.CharField(max_length=20)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_master_user_tenant', to='distribution_user.Tenant')),
            ],
            options={
                'ordering': ('account_type', 'name'),
            },
        ),
        migrations.CreateModel(
            name='accountingPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('key', models.CharField(max_length=5)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='period_master_user_tenant', to='distribution_user.Tenant')),
            ],
            options={
                'ordering': ('start',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='accountingperiod',
            unique_together=set([('key', 'tenant')]),
        ),
        migrations.AlterUniqueTogether(
            name='accountchart',
            unique_together=set([('key', 'tenant'), ('name', 'tenant')]),
        ),
    ]
