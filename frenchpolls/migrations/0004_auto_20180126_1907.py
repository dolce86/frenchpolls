# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-26 18:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frenchpolls', '0003_auto_20180126_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reponse',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frenchpolls.Question'),
        ),
    ]