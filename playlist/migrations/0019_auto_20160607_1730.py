# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0018_playgroup_logourl'),
    ]

    operations = [
        migrations.CreateModel(
            name='liveplaygroup_adv',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('channelid', models.CharField(max_length=20, null=True, verbose_name=b'\xe9\xa2\x91\xe9\x81\x93ID', blank=True)),
                ('advurl', models.CharField(default=b'', max_length=255, verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe5\x9b\xbe\xe7\x89\x87\xe4\xb8\x8b\xe8\xbd\xbd\xe5\x9c\xb0\xe5\x9d\x80')),
                ('livegroupid', models.ForeignKey(related_name='live_adv', to='playlist.liveplaygroup')),
            ],
        ),
        migrations.DeleteModel(
            name='playgroup',
        ),
    ]
