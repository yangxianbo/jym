# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0008_delete_playgroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='playgroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groupid', models.CharField(unique=True, max_length=20, verbose_name=b'\xe6\x92\xad\xe6\x94\xbe\xe7\xbb\x84ID')),
                ('livegroupid', models.CharField(max_length=20, null=True, verbose_name=b'\xe7\x9b\xb4\xe6\x92\xad\xe6\x92\xad\xe6\x94\xbe\xe7\xbb\x84ID', blank=True)),
                ('vodgroupid', models.CharField(max_length=20, null=True, verbose_name=b'\xe7\x82\xb9\xe6\x92\xad\xe6\x92\xad\xe6\x94\xbe\xe7\xbb\x84ID', blank=True)),
            ],
        ),
    ]
