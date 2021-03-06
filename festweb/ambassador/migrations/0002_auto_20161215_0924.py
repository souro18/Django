# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-15 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambassador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='EmailAdd',
            field=models.EmailField(default='null', max_length=254),
        ),
        migrations.AddField(
            model_name='signup',
            name='collegName',
            field=models.CharField(default='collegename', max_length=50),
        ),
        migrations.AddField(
            model_name='signup',
            name='collegeAddress',
            field=models.CharField(default='add', max_length=20),
        ),
        migrations.AddField(
            model_name='signup',
            name='facebookLink',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='innitaitives',
            field=models.TextField(default='null'),
        ),
        migrations.AlterField(
            model_name='signup',
            name='full_name',
            field=models.CharField(default='fullname', max_length=30),
        ),
    ]
