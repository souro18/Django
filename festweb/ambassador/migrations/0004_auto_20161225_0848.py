# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-25 08:48
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambassador', '0003_auto_20161216_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='PhoneNo',
            field=models.CharField(default=1234567890, max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_phonenumber', message='Please enter a valid phone number WITHOUT any PREFIX', regex='^[789]\\d{9}$')]),
        ),
        migrations.AlterField(
            model_name='signup',
            name='Email_Address',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='signup',
            name='college_Address',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='signup',
            name='college_Name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='signup',
            name='full_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='signup',
            name='innitaitives',
            field=models.TextField(),
        ),
    ]
