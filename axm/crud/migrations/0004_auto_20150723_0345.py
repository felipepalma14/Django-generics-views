# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20150723_0324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='habilitador',
            new_name='habilitado',
        ),
    ]
