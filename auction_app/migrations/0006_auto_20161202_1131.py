# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-02 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction_app', '0005_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='updated',
            field=models.DateTimeField(null=True),
        ),
    ]
