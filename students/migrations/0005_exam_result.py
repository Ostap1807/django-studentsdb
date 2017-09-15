# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_auto_20170913_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam_result',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('mark', models.IntegerField(verbose_name='Бал')),
                ('exam', models.ForeignKey(to='students.Exam', verbose_name='Іспит')),
                ('group', models.ForeignKey(to='students.Group', verbose_name='Група')),
                ('student', models.ForeignKey(to='students.Student', verbose_name='Студент')),
            ],
            options={
                'verbose_name': 'Результати іспиту',
            },
        ),
    ]
