# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-24 04:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distributor_user', '0014_auto_20170824_0723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
    ]
