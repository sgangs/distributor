# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 06:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_teacher', '0016_auto_20170320_1455'),
        ('school_user', '0017_tenant_no_of_profile'),
        ('school_hr', '0014_teacher_attendance_attendance_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='staff_leave',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('year', models.PositiveSmallIntegerField(verbose_name='Please enter start (year) of the academic year')),
                ('numbers', models.PositiveSmallIntegerField()),
                ('leave_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staffLeave_leaveType', to='school_hr.leave_type')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staffLeave_hr_teacher_teacher', to='school_teacher.Teacher')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staffLeave_hr_user_tenant', to='school_user.Tenant')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='staff_leave',
            unique_together=set([('teacher', 'leave_type', 'year')]),
        ),
    ]
