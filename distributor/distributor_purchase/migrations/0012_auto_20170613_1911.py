# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-13 13:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('distributor_master', '0007_auto_20170608_1118'),
        ('distributor_user', '0004_user_permission'),
        ('distributor_purchase', '0011_auto_20170609_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='debit_note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_id', models.CharField(blank=True, max_length=12)),
                ('note_type', models.CharField(choices=[(1, 'Goods Return'), (2, 'Payment Adjustment')], max_length=12)),
                ('supplier_invoice', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('vendor_name', models.CharField(db_index=True, max_length=200)),
                ('vendor_address', models.TextField(blank=True, null=True)),
                ('vendor_state', models.CharField(blank=True, max_length=4, null=True)),
                ('vendor_city', models.CharField(blank=True, max_length=50, null=True)),
                ('vendor_pin', models.CharField(blank=True, max_length=8, null=True)),
                ('warehouse_address', models.TextField()),
                ('warehouse_state', models.CharField(max_length=4)),
                ('warehouse_city', models.CharField(max_length=50)),
                ('warehouse_pin', models.CharField(max_length=8)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=12)),
                ('taxtotal', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('cgsttotal', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('sgsttotal', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('igsttotal', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('total', models.DecimalField(decimal_places=2, max_digits=12)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debitNote_purchase_user_tenant', to='distributor_user.Tenant')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='debitNote_purchase_master_vendor', to='distributor_master.Vendor')),
                ('warehouse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='debitNote_purchase_master_warehouse', to='distributor_master.Warehouse')),
            ],
        ),
        migrations.CreateModel(
            name='debit_note_line_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_sku', models.CharField(max_length=50)),
                ('vat_type', models.CharField(blank=True, max_length=15, null=True)),
                ('tax_percent', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('unit', models.CharField(max_length=20)),
                ('unit_multi', models.DecimalField(decimal_places=2, default=1, max_digits=5)),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tentative_sales_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('mrp', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='MRP')),
                ('cgst_percent', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('sgst_percent', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('igst_percent', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('cgst_value', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('sgst_value', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('igst_value', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('line_tax', models.DecimalField(decimal_places=2, max_digits=12)),
                ('line_total', models.DecimalField(decimal_places=2, max_digits=12)),
                ('debit_note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debitNoteLineItem_debitNote', to='distributor_purchase.debit_note')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='debitNoteLineItem_purchase_master_product', to='distributor_master.Product')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debitNoteLineItem_purchase_user_tenant', to='distributor_user.Tenant')),
            ],
        ),
        migrations.AlterField(
            model_name='receipt_line_item',
            name='vat_type',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]