# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='appinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('appid', models.CharField(unique=True, max_length=50)),
                ('appname', models.CharField(max_length=50, null=True, blank=True)),
                ('appdesc', models.CharField(max_length=255, null=True, blank=True)),
                ('appfolder', models.CharField(max_length=255, null=True, blank=True)),
                ('uptime', models.CharField(max_length=255, null=True, blank=True)),
                ('version', models.CharField(max_length=255, null=True, blank=True)),
                ('downloadurl', models.CharField(max_length=255, null=True, blank=True)),
                ('appsize', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
    ]
