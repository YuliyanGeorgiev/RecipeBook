# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-13 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_choice_choice_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=20)),
            ],
        ),
    ]
