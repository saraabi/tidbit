# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tidbit', '0002_auto_20150913_0301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='list',
            new_name='story_list',
        ),
    ]
