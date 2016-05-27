# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gname', models.CharField(max_length=255, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('members', models.CharField(max_length=255, verbose_name=b'\xe6\x88\x90\xe5\x91\x98')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('department', models.CharField(default=b'\xe6\x9c\xaa\xe7\x9f\xa5', max_length=255, verbose_name=b'\xe9\x83\xa8\xe9\x97\xa8')),
                ('mobile', models.CharField(default=b'\xe6\x9c\xaa\xe7\x9f\xa5', max_length=255, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe7\x94\xb5\xe8\xaf\x9d')),
                ('is_create', models.CharField(default=b'1', max_length=10, verbose_name=b'\xe6\x96\xb0\xe5\xa2\x9e')),
                ('is_delete', models.CharField(default=b'1', max_length=10, verbose_name=b'\xe5\x88\xa0\xe9\x99\xa4')),
                ('is_modify', models.CharField(default=b'1', max_length=10, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9')),
                ('is_check', models.CharField(default=b'1', max_length=10, verbose_name=b'\xe6\x9f\xa5\xe8\xaf\xa2')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
