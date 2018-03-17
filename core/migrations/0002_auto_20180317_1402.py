# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='picture',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='goods',
            name='picture',
            field=models.CharField(default='', max_length=128),
        ),
    ]
