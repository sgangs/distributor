# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-06 02:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('distributor_user', '0022_tenant_distributor_sales_policy'),
        ('distributor_account', '0030_auto_20180207_2258'),
    ]

    operations = [
        migrations.CreateModel(
            name='account_relation',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('relation', models.PositiveSmallIntegerField(choices=[(1, 'Main Purchase Account'), (2, 'Main Sales Account'), (3, 'Main Purchase Cash Discount Account'), (4, 'Main Sales Cash Discount Account')], db_index=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='account',
            options={},
        ),
        migrations.AddField(
            model_name='account_relation',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accountRelation_account', to='distributor_account.Account'),
        ),
        migrations.AddField(
            model_name='account_relation',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accountRelation_account_user_tenant', to='distributor_user.Tenant'),
        ),
        migrations.AlterUniqueTogether(
            name='account_relation',
            unique_together=set([('relation', 'tenant')]),
        ),
    ]