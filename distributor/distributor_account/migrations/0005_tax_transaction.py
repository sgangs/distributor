# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-20 04:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('distributor_master', '0002_auto_20170517_1647'),
        ('distributor_user', '0002_auto_20170517_1647'),
        ('distributor_account', '0004_auto_20170517_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='tax_transaction',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('transaction_type', models.PositiveSmallIntegerField(db_index=True)),
                ('tax_type', models.CharField(db_index=True, max_length=5)),
                ('tax_percent', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('tax_value', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('product_name', models.CharField(db_index=True, max_length=200)),
                ('transaction_bill_id', models.BigIntegerField(blank=True, db_index=True, null=True)),
                ('date', models.DateField(db_index=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taxTransaction_account_master_product', to='distributor_master.Product')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taxTransaction_account_user_tenant', to='distributor_user.Tenant')),
            ],
        ),
    ]
