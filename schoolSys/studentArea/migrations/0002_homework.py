# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-04 15:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentArea', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('homework_title', models.CharField(max_length=200)),
                ('homework_content', models.TextField()),
                ('grade', models.CharField(max_length=200)),
                ('other_homework_details', models.TextField()),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentArea.Students')),
            ],
        ),
    ]