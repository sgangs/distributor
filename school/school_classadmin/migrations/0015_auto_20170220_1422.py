# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-20 08:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_student', '0017_auto_20170219_1615'),
        ('school_eduadmin', '0026_auto_20170220_1422'),
        ('school_classadmin', '0014_auto_20170219_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='exam_final_report',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('year', models.PositiveSmallIntegerField(db_index=True)),
                ('remarks', models.TextField()),
                ('passed', models.BooleanField()),
                ('class_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examFinalReport_classadmin_eduadmin_classSection', to='school_eduadmin.class_section')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examFinalReport_classadmin_student_student', to='school_student.Student')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examFinalReport_classadmin_user_tenant', to='school_user.Tenant')),
            ],
        ),
        migrations.CreateModel(
            name='exam_year_final',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(choices=[('Life', 'Life Skills'), ('Work', 'Work Education'), ('VPA', 'Visual & Performing Art'), ('AV', 'Attitude & Values'), ('CSA', 'Co-Scholastic Actitivies'), ('HPE', 'Health & Physical Education')], max_length=4)),
                ('final_score', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('grade', models.CharField(blank=True, max_length=4, null=True)),
                ('grade_point', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('final_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examYearFinal_examFinalReport', to='school_user.Tenant')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examYearFinal_classadmin_user_tenant', to='school_user.Tenant')),
            ],
        ),
        migrations.RemoveField(
            model_name='exam_report',
            name='year',
        ),
        migrations.AddField(
            model_name='exam_coscholastic_report',
            name='grade_point',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='exam_coscholastic_report',
            name='total',
            field=models.PositiveSmallIntegerField(blank=True, default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='exam_report',
            name='grade_point',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='exam_coscholastic_report',
            name='final_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='exam_report',
            name='final_score',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='exam_report',
            name='grade',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        # migrations.RemoveField(
        #     model_name='exam_coscholastic_report',
        #     name='year',
        # ),
        migrations.AlterUniqueTogether(
            name='exam_coscholastic_report',
            unique_together=set([('student', 'exam', 'topic', 'tenant')]),
        ),
        migrations.AlterUniqueTogether(
            name='exam_year_final',
            unique_together=set([('final_report', 'topic', 'tenant')]),
        ),
        migrations.AlterUniqueTogether(
            name='exam_final_report',
            unique_together=set([('student', 'year', 'tenant')]),
        ),
    ]