# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matriculas', '0003_auto_20171116_0812'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('creditos', models.PositiveSmallIntegerField()),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
    ]
