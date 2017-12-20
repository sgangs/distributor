# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-24 04:26
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('distributor_user', '0015_remove_user_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_authorization',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), blank=True, null=True, size=None),
        ),
    ]