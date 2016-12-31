# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-17 03:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school_student', '0006_student_dob'),
        ('school_user', '0004_auto_20161217_0924'),
        ('school_genadmin', '0004_auto_20161208_2258'),
        ('school_teacher', '0003_auto_20161209_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_index=True)),
                ('author', models.TextField(blank=True, db_index=True, null=True)),
                ('publisher', models.TextField(blank=True, null=True)),
                ('edition', models.CharField(blank=True, max_length=40, null=True)),
                ('isbn', models.CharField(blank=True, db_index=True, max_length=18, null=True)),
                ('remark', models.TextField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=30, null=True, verbose_name='Rack location')),
                ('purchased_on', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('school_book_code', models.CharField(blank=True, max_length=40, null=True, verbose_name='Internal Book Code')),
                ('key', models.CharField(max_length=12)),
                ('slug', models.SlugField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='book_issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued_on', models.DateField()),
                ('remark', models.TextField(blank=True, null=True)),
                ('key', models.CharField(max_length=12)),
                ('returned', models.BooleanField()),
                ('slug', models.SlugField(max_length=35)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookIssue_book', to='school_library.Book')),
            ],
        ),
        migrations.CreateModel(
            name='book_return',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('returned_on', models.DateField()),
                ('maximum_return_date', models.DateField()),
                ('remark', models.TextField(blank=True, null=True)),
                ('issue_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookReturn_bookIssue', to='school_library.book_issue')),
            ],
        ),
        migrations.CreateModel(
            name='issue_period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.PositiveSmallIntegerField(default=7, verbose_name='No of days book will be issued')),
                ('slug', models.SlugField(max_length=30)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issuePeriod_library_user_tenant', to='school_user.Tenant')),
            ],
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=55)),
                ('librarian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='librarian_library_teacher_teacher', to='school_teacher.Teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=15, verbose_name='Room name/no.')),
                ('slug', models.SlugField(max_length=40)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='library_library_user_tenant', to='school_user.Tenant')),
            ],
        ),
        migrations.AddField(
            model_name='librarian',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='librarian_library', to='school_library.Library'),
        ),
        migrations.AddField(
            model_name='librarian',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='librarian_library_user_tenant', to='school_user.Tenant'),
        ),
        migrations.AddField(
            model_name='book_return',
            name='return_entry_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookReturn_librarian', to='school_library.Librarian'),
        ),
        migrations.AddField(
            model_name='book_return',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookReturn_library_user_tenant', to='school_user.Tenant'),
        ),
        migrations.AddField(
            model_name='book_issue',
            name='issue_period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookIssue_issuePeriod', to='school_library.issue_period'),
        ),
        migrations.AddField(
            model_name='book_issue',
            name='issued_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookIssue_librarian', to='school_library.Librarian'),
        ),
        migrations.AddField(
            model_name='book_issue',
            name='issued_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookIssue_library_student_student', to='school_student.Student'),
        ),
        migrations.AddField(
            model_name='book_issue',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookIssue_library_user_tenant', to='school_user.Tenant'),
        ),
        migrations.AddField(
            model_name='book',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_library', to='school_library.Library'),
        ),
        migrations.AddField(
            model_name='book',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_library_genadmin_subject', to='school_genadmin.Subject'),
        ),
        migrations.AddField(
            model_name='book',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_library_user_tenant', to='school_user.Tenant'),
        ),
        migrations.AlterUniqueTogether(
            name='library',
            unique_together=set([('room', 'tenant')]),
        ),
        migrations.AlterUniqueTogether(
            name='librarian',
            unique_together=set([('library', 'librarian', 'tenant')]),
        ),
        migrations.AlterUniqueTogether(
            name='issue_period',
            unique_together=set([('period', 'tenant')]),
        ),
        migrations.AlterUniqueTogether(
            name='book_return',
            unique_together=set([('issue_details', 'tenant')]),
        ),
        migrations.AlterUniqueTogether(
            name='book_issue',
            unique_together=set([('key', 'tenant')]),
        ),
        migrations.AlterUniqueTogether(
            name='book',
            unique_together=set([('key', 'tenant')]),
        ),
    ]
