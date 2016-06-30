# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='address',
            field=models.CharField(max_length=40, verbose_name='住址或单位'),
        ),
        migrations.AlterField(
            model_name='content',
            name='date_of_birth',
            field=models.DateField(verbose_name='生日'),
        ),
        migrations.AlterField(
            model_name='content',
            name='doctor',
            field=models.CharField(max_length=20, verbose_name='主治医师'),
        ),
        migrations.AlterField(
            model_name='content',
            name='job',
            field=models.CharField(max_length=20, verbose_name='职业'),
        ),
        migrations.AlterField(
            model_name='content',
            name='name',
            field=models.CharField(max_length=10, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='content',
            name='sex',
            field=models.CharField(max_length=20, choices=[('女', 'FM'), ('男', 'M')]),
        ),
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(max_length=30, verbose_name='医院'),
        ),
    ]
