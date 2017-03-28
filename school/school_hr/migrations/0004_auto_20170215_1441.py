# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-15 09:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_teacher', '0012_auto_20170215_0948'),
        ('school_hr', '0003_auto_20170204_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='cadre_leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Please enter (year for) start of the academic year')),
                ('numbers', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='staff_cadre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staffCadre_hr_user_tenant', to='school_user.Tenant')),
            ],
        ),
        migrations.CreateModel(
            name='staff_cadre_linking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cadre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staffCadreLinking_staffCadre', to='school_hr.staff_cadre')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staffCadreLinking_hr_teacher_teacher', to='school_teacher.Teacher')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staffCadreLinking_hr_user_tenant', to='school_user.Tenant')),
            ],
        ),
        migrations.AddField(
            model_name='cadre_leave',
            name='cadre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cadreLeave_staffCadre', to='school_hr.staff_cadre'),
        ),
        migrations.AddField(
            model_name='cadre_leave',
            name='leave_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cadreLeave_leaveType', to='school_hr.leave_type'),
        ),
        migrations.AddField(
            model_name='cadre_leave',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cadreLeave_hr_user_tenant', to='school_user.Tenant'),
        ),
        migrations.AlterUniqueTogether(
            name='staff_cadre_linking',
            unique_together=set([('cadre', 'teacher')]),
        ),
        migrations.AlterUniqueTogether(
            name='staff_cadre',
            unique_together=set([('name', 'tenant')]),
        ),
        migrations.AlterUniqueTogether(
            name='cadre_leave',
            unique_together=set([('cadre', 'leave_type', 'year')]),
        ),
    ]