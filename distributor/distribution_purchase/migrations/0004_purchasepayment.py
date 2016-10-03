# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-02 14:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('distribution_purchase', '0003_auto_20161001_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='purchasePayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=12)),
                ('collected_on', models.DateTimeField(null=True)),
                ('invoice_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchasePayment_purchaseInvoice', to='distribution_purchase.purchaseInvoice')),
            ],
        ),
    ]
