# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 11:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_eduadmin', '0028_auto_20170226_1724'),
        ('school_classadmin', '0016_remove_exam_coscholastic_report_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam_coscholastic_report',
            old_name='curricular_type',
            new_name='details',
        ),
        migrations.RemoveField(
            model_name='exam_coscholastic_report',
            name='final_score',
        ),
        migrations.AddField(
            model_name='exam_coscholastic_report',
            name='sl_no',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exam_coscholastic_report',
            name='term',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='examCoscholasticReport_classadmin_eduadmin_Term', to='school_eduadmin.Term'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exam_coscholastic_report',
            name='grade',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='exam_coscholastic_report',
            name='grade_point',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='exam_coscholastic_report',
            name='topic',
            field=models.CharField(choices=[('Life', '2(A) Life Skills'), ('Work', '2(B) Work Education'), ('VPA', '2(C) Visual & Performing Art'), ('AV', '2(D) Attitude & Values'), ('CSA', '3(A) Co-Scholastic Actitivies'), ('HPE', '3(B) Health & Physical Education')], max_length=4),
        ),
        migrations.AlterField(
            model_name='exam_coscholastic_report',
            name='total',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exam_year_final',
            name='topic',
            field=models.CharField(choices=[('Life', '2(A) Life Skills'), ('Work', '2(B) Work Education'), ('VPA', '2(C) Visual & Performing Art'), ('AV', '2(D) Attitude & Values'), ('CSA', '3(A) Co-Scholastic Actitivies'), ('HPE', '3(B) Health & Physical Education')], max_length=4),
        ),
    ]