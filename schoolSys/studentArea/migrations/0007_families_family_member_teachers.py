# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-05 08:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentArea', '0006_auto_20180105_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='Families',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_name', models.CharField(max_length=200)),
                ('head_of_family_parent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentArea.Parents')),
            ],
        ),
        migrations.CreateModel(
            name='Family_member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_or_student_member', models.CharField(max_length=200)),
                ('family_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentArea.Families')),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentArea.Parents')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentArea.Students')),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.BooleanField()),
                ('first_name', models.CharField(max_length=200)),
                ('middle_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('other_teacher_details', models.TextField()),
                ('school_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentArea.Schools')),
            ],
        ),
    ]