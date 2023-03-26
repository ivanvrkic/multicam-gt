# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marker', '0008_delete_rectangle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workerID', models.PositiveIntegerField(default=0)),
                ('frameNB', models.PositiveSmallIntegerField(default=0)),
                ('validationoCode', models.PositiveIntegerField(default=0)),
                ('finished', models.BooleanField(default=False)),
                ('state', models.IntegerField(default=-1)),
            ],
        ),
    ]
