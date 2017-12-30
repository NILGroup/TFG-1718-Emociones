# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-22 11:05
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emocion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('palabra', models.CharField(max_length=30)),
                ('porcentajes', models.CharField(max_length=100, validators=[(django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.'), '0,17,33,50,67,83,100', None)])),
            ],
            options={
                'ordering': ('palabra',),
            },
        ),
    ]