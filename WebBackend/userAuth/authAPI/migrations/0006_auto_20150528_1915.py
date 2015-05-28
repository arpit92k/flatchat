# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authAPI', '0005_userprofile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default='none', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='budget',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='locality',
            field=models.CharField(max_length=500, blank=True),
        ),
    ]
