# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-26 17:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frenchpolls', '0002_auto_20180117_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reponse',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reponse', to='frenchpolls.Question'),
        ),
    ]
