# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-09 05:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_fees', '0006_auto_20170125_1936'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='student_fee_payment',
            unique_together=set([('student', 'month', 'year', 'tenant')]),
        ),
    ]
