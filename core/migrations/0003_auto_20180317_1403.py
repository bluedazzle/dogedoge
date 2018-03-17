# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180317_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gift',
            name='picture',
            field=models.CharField(default='', max_length=128, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='goods',
            name='picture',
            field=models.CharField(default='', max_length=128, null=True, blank=True),
        ),
    ]
