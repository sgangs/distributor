# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-04 09:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_user', '0006_auto_20170104_1019'),
        ('school_genadmin', '0007_auto_20161227_0744'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=15)),
                ('slug', models.SlugField()),
                ('class_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batch_classGroup', to='school_genadmin.class_group')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='batch_genadmin_user_tenant', to='school_user.Tenant')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='batch',
            unique_together=set([('name', 'tenant')]),
        ),
    ]
