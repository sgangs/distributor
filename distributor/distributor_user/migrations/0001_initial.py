# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-17 03:17
from __future__ import unicode_literals

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('aadhaar_no', models.CharField(blank=True, max_length=20, verbose_name='Aadhaar Number')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='Phone Number')),
                ('user_type', models.CharField(choices=[('Owner', 'Owner'), ('Salesperson', 'Salesperson')], max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'abstract': False,
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Name of your company')),
                ('pan', models.PositiveIntegerField(blank=True, null=True, verbose_name='PAN Number')),
                ('tin', models.PositiveIntegerField(blank=True, null=True, verbose_name='TIN Number')),
                ('cst', models.PositiveIntegerField(blank=True, null=True, verbose_name='CST Number')),
                ('gst', models.PositiveIntegerField(blank=True, null=True, verbose_name='GST Number')),
                ('address_1', models.CharField(max_length=200, verbose_name='Address Line 1')),
                ('address_2', models.CharField(blank=True, max_length=200, null=True, verbose_name='Address Line 2')),
                ('state', models.CharField(choices=[('ANI', 'Andaman & Nicobar Island'), ('AP', 'Andhra Pradesh'), ('AN', 'Andaman & Nicobar Island'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BI', 'Bihar'), ('CHN', 'Chandigarh'), ('CHT', 'Chattisgarh'), ('DNH', 'Dadra & Nagar Haveli'), ('DD', 'Daman & Diu'), ('DEL', 'National Capital Territory of Delhi'), ('GOA', 'Goa'), ('GUJ', 'Gujrat'), ('HAR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu & Kashmir'), ('JHA', 'Jharkhand'), ('KAR', 'Karnataka'), ('KER', 'Kerala'), ('LAK', 'Lakshadweep'), ('MP', 'Madhya Pradesh'), ('MAH', 'Maharashtra'), ('MAN', 'Manipur'), ('MEG', 'Meghalaya'), ('MIZ', 'Mizoram'), ('NAG', 'Nagaland'), ('OD', 'Odisha'), ('PUD', 'Puducherry'), ('PUN', 'Punjab'), ('RAJ', 'Rajashtan'), ('SIK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TEL', 'Telengana'), ('TRI', 'Tripura'), ('UP', 'Uttar Pradesh'), ('UTT', 'Uttarkhand'), ('WB', 'West Bengal')], max_length=4)),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('pin', models.CharField(max_length=8, verbose_name='Pincode')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Official Email Address')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('slug', models.SlugField(max_length=20)),
                ('key', models.CharField(max_length=20, unique=True, verbose_name='Unique ID/Short Name of Company')),
                ('registered_on', models.DateTimeField()),
                ('no_of_profile', models.PositiveIntegerField(default=0)),
                ('account', models.CharField(choices=[('Basic', 'Basic'), ('SMS_Active', 'SMS_Active')], default='Basic', max_length=12)),
                ('paid', models.BooleanField(verbose_name='Has the tenant paid?')),
                ('trial', models.BooleanField(verbose_name='Is the tenant under trail?')),
                ('trial_from', models.DateField(blank=True, null=True)),
                ('trial_to', models.DateField(blank=True, null=True)),
                ('paid_until', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_tenant', to='distributor_user.Tenant'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
