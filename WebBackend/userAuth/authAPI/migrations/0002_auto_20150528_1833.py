# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authAPI', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_login',
            field=models.DateTimeField(null=True, verbose_name='last login', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(default='pwd', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
