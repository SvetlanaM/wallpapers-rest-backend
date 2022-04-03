# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-06 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inapp',
            name='payment',
        ),
        migrations.AddField(
            model_name='inapp',
            name='currency',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
