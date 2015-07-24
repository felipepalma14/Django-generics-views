# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_auto_20150723_0345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='marca_codigo',
            new_name='marca',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='usuario_codigo',
            new_name='usuario',
        ),
    ]
