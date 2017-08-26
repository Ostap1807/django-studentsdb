# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(verbose_name="Ім'я", max_length=256)),
                ('last_name', models.CharField(verbose_name='Прізвище', max_length=256)),
                ('middle_name', models.CharField(max_length=256, verbose_name='По-батькові', blank=True, default='')),
                ('birthday', models.DateField(verbose_name='Дата народження', null=True)),
                ('photo', models.ImageField(upload_to='', verbose_name='Фото', blank=True, null=True)),
                ('ticket', models.CharField(verbose_name=False, max_length=256)),
                ('notes', models.TextField(verbose_name='Додаткові нотатки', blank=True)),
            ],
        ),
    ]
