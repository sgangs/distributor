# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-01 07:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distribution_master', '0012_auto_20161001_0316'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='warehouse',
            options={'ordering': ('-default', 'address', 'status')},
        ),
    ]
