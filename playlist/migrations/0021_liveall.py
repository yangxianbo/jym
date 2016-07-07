# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0020_liveplaygroup_adv_advstate'),
    ]

    operations = [
        migrations.CreateModel(
            name='liveall',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('liverelate_group', models.TextField(default=b'', max_length=1000, verbose_name=b'\xe6\x92\xad\xe6\x94\xbe\xe5\xa4\xa7\xe7\xbb\x84\xe5\x85\xb3\xe8\x81\x94\xe7\x9a\x84\xe5\xb0\x8f\xe7\xbb\x84')),
                ('livedesc', models.CharField(max_length=255, null=True, verbose_name=b'\xe6\x92\xad\xe6\x94\xbe\xe5\xa4\xa7\xe7\xbb\x84\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
            ],
        ),
    ]
