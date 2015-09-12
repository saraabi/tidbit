# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tidbit', '0003_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='list',
            field=models.ForeignKey(default=None, to='tidbit.List'),
        ),
    ]
