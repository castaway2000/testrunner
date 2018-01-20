# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-01-20 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testrunner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=16)),
                ('port', models.IntegerField()),
                ('name', models.CharField(max_length=256)),
            ],
        ),
    ]
