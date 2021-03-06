# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 07:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_student', '0018_auto_20170221_1953'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school_classadmin', '0018_auto_20170227_0102'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_remark',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('visible_to', models.PositiveSmallIntegerField(choices=[(1, 'Student'), (2, 'Parent'), (3, 'Both')])),
                ('comment', models.TextField()),
                ('remarked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentRemarkBy_classadmin_student_student', to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentRemark_classadmin_student_student', to='school_student.Student')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentRemark_classadmin_user_tenant', to='school_user.Tenant')),
            ],
        ),
        migrations.CreateModel(
            name='student_remark_comment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('commentor_type', models.CharField(choices=[('Master', 'Master'), ('Teacher', 'Teacher'), ('Admin', 'Admin'), ('Principal', 'Principal'), ('Account', 'Account'), ('Collector', 'Fee Collector'), ('Student', 'Student'), ('Parent', 'Parent')], max_length=10)),
                ('comment', models.TextField()),
                ('commented_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentRemarkCommentBy_classadmin_student_student', to=settings.AUTH_USER_MODEL)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentRemarkComments_classadmin_user_tenant', to='school_user.Tenant')),
            ],
        ),
    ]
