# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tidbit', '0003_auto_20150913_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='story_list',
            field=models.ForeignKey(blank=True, to='tidbit.List', null=True),
        ),
    ]
