# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-02 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='id',
        ),
        migrations.AddField(
            model_name='item',
            name='item_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
