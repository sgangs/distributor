# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-19 15:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('distributor_master', '0014_product_barcode'),
        ('distributor_user', '0007_auto_20170616_1206'),
        ('distributor_inventory', '0006_auto_20170614_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='inventory_wastage',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('purchase_price', models.DecimalField(blank=True, db_index=True, decimal_places=2, max_digits=10, null=True)),
                ('inventory_average_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('quantity', models.PositiveSmallIntegerField(db_index=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventoryWastage_inventory_master_product', to='distributor_master.Product')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventoryWastage_inventory_user_tenant', to='distributor_user.Tenant')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventoryWastage_inventory_master_warehouse', to='distributor_master.Warehouse')),
            ],
        ),
        migrations.AlterField(
            model_name='inventory_transfer',
            name='in_transit',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]