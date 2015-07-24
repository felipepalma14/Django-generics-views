# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=60)),
                ('preco', models.FloatField()),
                ('quantidade', models.IntegerField()),
                ('marca_codigo', models.ForeignKey(to='crud.Marca')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=60, validators=[django.core.validators.RegexValidator(b'^[a-zA-Z ]*$', b'Only letters are allowed')])),
                ('email', models.EmailField(unique=True, max_length=40)),
                ('senha', models.CharField(max_length=600)),
                ('habilitador', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='produto',
            name='usuario_codigo',
            field=models.ForeignKey(to='crud.Usuario'),
        ),
    ]
