# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-16 19:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distribution_accounts', '0004_auto_20160915_1747'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='journalentry',
            options={'ordering': ('journal', '-transaction_type')},
        ),
        migrations.RenameField(
            model_name='journal',
            old_name='remarks',
            new_name='journal_type',
        ),
    ]
