# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-27 02:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_student', '0021_auto_20170316_1139'),
        ('school_genadmin', '0030_auto_20170325_0908'),
        ('school_user', '0017_tenant_no_of_profile'),
        ('school_eduadmin', '0041_auto_20170323_2055'),
        ('school_classadmin', '0022_auto_20170323_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='term_report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField(db_index=True)),
                ('term_score', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('term_grade', models.CharField(blank=True, max_length=4, null=True)),
                ('term_grade_point', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('class_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='termReport_classadmin_eduadmin_classSection', to='school_eduadmin.class_section')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='termReport_classadmin_student_student', to='school_student.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='termReport_classadmin_genadmin_subject', to='school_genadmin.Subject')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='termReport_classadmin_user_tenant', to='school_user.Tenant')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='termReport_classadmin_eduadmin_term', to='school_eduadmin.Term')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='exam_final_report',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='exam_final_report',
            name='class_section',
        ),
        migrations.RemoveField(
            model_name='exam_final_report',
            name='student',
        ),
        migrations.RemoveField(
            model_name='exam_final_report',
            name='tenant',
        ),
        migrations.AlterUniqueTogether(
            name='exam_year_final',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='exam_year_final',
            name='final_report',
        ),
        migrations.RemoveField(
            model_name='exam_year_final',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='exam_year_final',
            name='tenant',
        ),
        migrations.AlterField(
            model_name='exam_report',
            name='year',
            field=models.PositiveSmallIntegerField(db_index=True),
        ),
        migrations.DeleteModel(
            name='exam_final_report',
        ),
        migrations.DeleteModel(
            name='exam_year_final',
        ),
        migrations.AlterUniqueTogether(
            name='term_report',
            unique_together=set([('term', 'subject', 'year', 'tenant')]),
        ),
    ]
