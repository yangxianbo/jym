# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsys', '0006_auto_20160412_0043'),
    ]

    operations = [
        migrations.CreateModel(
            name='group_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groupname', models.CharField(default=b'basegroup', unique=True, max_length=255, verbose_name=b'\xe7\xbb\x84\xe5\x90\x8d')),
            ],
        ),
        migrations.AddField(
            model_name='machine_info',
            name='groupid',
            field=models.ManyToManyField(to='authsys.group_info'),
        ),
    ]
