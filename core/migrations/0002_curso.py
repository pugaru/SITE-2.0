# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=10)),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
    ]
