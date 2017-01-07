# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-06 16:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_account', '0012_auto_20170106_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account_year',
            name='accounting_period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accountYear_accountingPeriod', to='school_account.accounting_period'),
        ),
        migrations.AlterField(
            model_name='account_year',
            name='opening_credit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Opening Credit Balance'),
        ),
        migrations.AlterField(
            model_name='account_year',
            name='opening_debit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Opening Debit Balance'),
        ),
        migrations.AlterUniqueTogether(
            name='account_year',
            unique_together=set([('account', 'accounting_period', 'tenant')]),
        ),
    ]
