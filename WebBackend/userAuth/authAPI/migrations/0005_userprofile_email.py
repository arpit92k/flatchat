# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authAPI', '0004_remove_userprofile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='pwd', unique=True, max_length=254, verbose_name=b'email address', db_index=True),
            preserve_default=False,
        ),
    ]
