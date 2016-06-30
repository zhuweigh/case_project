# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=30, verbose_name='Hospital')),
                ('sex', models.CharField(max_length=20, choices=[('Woman', 'FM'), ('Man', 'M')])),
                ('age', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=10, verbose_name='Name')),
                ('date_of_birth', models.DateField(verbose_name='Birth')),
                ('job', models.CharField(max_length=20, verbose_name='Job')),
                ('address', models.CharField(max_length=40, verbose_name='Address or Unit')),
                ('description', models.TextField()),
                ('result', models.CharField(max_length=3)),
                ('doctor', models.CharField(max_length=20, verbose_name='Doctor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
