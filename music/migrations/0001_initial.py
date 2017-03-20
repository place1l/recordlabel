# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compilation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_title', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(max_length=10)),
                ('artist', models.CharField(max_length=200)),
                ('album_title', models.CharField(max_length=200)),
                ('track_title', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=500)),
                ('track', models.CharField(max_length=1000)),
                ('track_pic', models.CharField(max_length=1000)),
            ],
        ),
    ]