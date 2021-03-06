# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-30 03:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_user', '0004_auto_20161217_0924'),
        ('school_genadmin', '0007_auto_20161227_0744'),
        ('school_fees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='group_default_fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField(db_index=True)),
                ('slug', models.SlugField()),
                ('classgroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groupDefaultFee_fees_genadmin_classGroup', to='school_genadmin.class_group')),
                ('monthly_fee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groupDefaultFee_monthlyFee', to='school_fees.monthly_fee')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groupDefaultFee_fees_user_tenant', to='school_user.Tenant')),
                ('yearly_fee', models.ManyToManyField(db_index=True, related_name='groupDefaultFee_yearlyFee', to='school_fees.yearly_fee')),
            ],
        ),
        migrations.AlterField(
            model_name='student_fee',
            name='slug',
            field=models.SlugField(max_length=56),
        ),
        migrations.AlterUniqueTogether(
            name='student_fee',
            unique_together=set([('student', 'monthly_fee', 'year', 'tenant')]),
        ),
        migrations.AlterUniqueTogether(
            name='group_default_fee',
            unique_together=set([('classgroup', 'monthly_fee', 'year', 'tenant')]),
        ),
    ]
