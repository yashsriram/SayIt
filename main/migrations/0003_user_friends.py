# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-11 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_usertousermessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(to='main.User'),
        ),
    ]
