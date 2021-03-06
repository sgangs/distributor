# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-06 11:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_account', '0009_auto_20170106_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='account_year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opening_debit', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('opening_credit', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accountYear_account', to='school_account.Account')),
                ('accounting_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accountYear_accountingPeriod', to='school_account.Account')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accountYear_account_user_tenant', to='school_user.Tenant')),
            ],
        ),
    ]
