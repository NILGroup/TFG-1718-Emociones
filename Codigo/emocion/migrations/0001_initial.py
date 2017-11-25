# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 10:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emocion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('palabra', models.CharField(blank=True, default='', max_length=30)),
                ('porcentajes', models.CommaSeparatedIntegerField(max_length=100)),
                ('emocion_mayor', models.CharField(choices=[(0, 'TRISTEZA'), (1, 'MIEDO'), (2, 'ALEGRIA'), (3, 'ENFADO'), (4, 'SORPRESA'), (5, 'NEUTRAL')], default='NEUTRAL', max_length=10)),
            ],
        ),
    ]
