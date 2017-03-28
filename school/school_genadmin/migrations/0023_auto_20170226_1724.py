# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 11:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_genadmin', '0022_auto_20170219_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='grade_table',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, verbose_name='Subject Name')),
                ('grade_type', models.CharField(choices=[('S', 'Scholastic'), ('C', 'Co-scholastic')], max_length=1, verbose_name='Type of grade?')),
                ('marks', models.PositiveSmallIntegerField()),
                ('grade', models.CharField(max_length=4)),
                ('grade_point', models.DecimalField(decimal_places=2, max_digits=4)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gradeTable_genadmin_user_tenant', to='school_user.Tenant')),
            ],
        ),
        migrations.CreateModel(
            name='notice_board',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('details', models.TextField()),
                ('show_from', models.DateField()),
                ('show_until', models.DateField()),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='noticeBoard_eduadmin_user_tenant', to='school_user.Tenant')),
            ],
            options={
                'ordering': ('show_from', 'show_until'),
            },
        ),
        migrations.AddField(
            model_name='class_group',
            name='standard',
            field=models.IntegerField(choices=[(-6, 'Lower Nusrsery'), (-5, 'Nursery'), (-4, 'Upper Nursery'), (-3, 'Lower KG'), (-2, 'Kindergarten'), (-1, 'Upper KG'), (1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Foure'), (5, 'Five'), (6, 'Six'), (7, 'Seven'), (8, 'Eight'), (9, 'Nine'), (10, 'Ten'), (11, 'Eleven'), (12, 'Twelve')], default=1),
        ),
        migrations.AddField(
            model_name='subject',
            name='is_additional',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='annual_calender',
            name='event_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Holiday'), (2, 'Exam'), (3, 'Exception'), (4, 'Others')], default='1', verbose_name='Event type'),
        ),
        migrations.AlterUniqueTogether(
            name='grade_table',
            unique_together=set([('grade_type', 'tenant')]),
        ),
    ]