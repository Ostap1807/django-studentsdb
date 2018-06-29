# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_auto_20180111_1101'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Student', 'verbose_name_plural': 'Students'},
        ),
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(verbose_name='Birthday', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(verbose_name='First Name', max_length=256),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(verbose_name='Last Name', max_length=256),
        ),
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(max_length=256, default='', verbose_name='Middle Name', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='notes',
            field=models.TextField(verbose_name='Extra Notes', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='photo',
            field=models.ImageField(verbose_name='Photo', blank=True, upload_to='', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Group', to='students.Group', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='ticket',
            field=models.CharField(verbose_name='Ticket', max_length=256),
        ),
    ]
