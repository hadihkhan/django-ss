# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-16 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.BooleanField()),
                ('first_name', models.CharField(max_length=200)),
                ('middle_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
                ('Other_student_details', models.TextField()),
            ],
        ),
    ]