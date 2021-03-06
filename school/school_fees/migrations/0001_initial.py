# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-29 14:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school_account', '0001_initial'),
        ('school_user', '0004_auto_20161217_0924'),
        ('school_student', '0008_auto_20161221_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='monthly_fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('key', models.CharField(db_index=True, max_length=12)),
                ('slug', models.SlugField()),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monthlyFee_fees_user_tenant', to='school_user.Tenant')),
            ],
        ),
        migrations.CreateModel(
            name='monthly_fee_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monthlyFeeList_fees_account_account', to='school_account.Account')),
                ('monthly_fee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monthlyFeeList_monthlyFee', to='school_fees.monthly_fee')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monthlyFeeList_fees_user_tenant', to='school_user.Tenant')),
            ],
        ),
        migrations.CreateModel(
            name='student_fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField(db_index=True)),
                ('slug', models.SlugField()),
                ('monthly_fee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentFee_monthlyFee', to='school_fees.monthly_fee')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentFee_fees_student_student', to='school_student.Student')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentFee_fees_user_tenant', to='school_user.Tenant')),
            ],
        ),
        migrations.CreateModel(
            name='yearly_fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('key', models.CharField(db_index=True, max_length=12)),
                ('slug', models.SlugField()),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yearlyFee_fees_user_tenant', to='school_user.Tenant')),
            ],
        ),
        migrations.CreateModel(
            name='yearly_fee_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('month', models.CharField(max_length=9)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yearlyFeeList_fees_account_account', to='school_account.Account')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yearlyFeeList_fees_user_tenant', to='school_user.Tenant')),
                ('yearly_fee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yearlyFeeList_monthlyFee', to='school_fees.yearly_fee')),
            ],
        ),
        migrations.AddField(
            model_name='student_fee',
            name='yearly_fee',
            field=models.ManyToManyField(db_index=True, related_name='studentFee_yearlyFee', to='school_fees.yearly_fee'),
        ),
        migrations.AlterUniqueTogether(
            name='yearly_fee_list',
            unique_together=set([('yearly_fee', 'account')]),
        ),
        migrations.AlterUniqueTogether(
            name='yearly_fee',
            unique_together=set([('key', 'tenant')]),
        ),
        migrations.AlterUniqueTogether(
            name='student_fee',
            unique_together=set([('student', 'monthly_fee', 'tenant')]),
        ),
        migrations.AlterUniqueTogether(
            name='monthly_fee_list',
            unique_together=set([('monthly_fee', 'account')]),
        ),
        migrations.AlterUniqueTogether(
            name='monthly_fee',
            unique_together=set([('key', 'tenant')]),
        ),
    ]
