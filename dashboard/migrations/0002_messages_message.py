# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='message',
            field=models.CharField(default='Hi', max_length=1000),
            preserve_default=False,
        ),
    ]
