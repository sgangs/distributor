# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-17 07:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distribution_accounts', '0005_auto_20160916_1936'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='accountchart',
            unique_together=set([('key', 'name', 'tenant')]),
        ),
    ]
