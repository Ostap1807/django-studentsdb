# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Група', max_length=256)),
                ('notes', models.TextField(blank=True, verbose_name='Додаткові нотатки')),
            ],
            options={
                'verbose_name_plural': 'Групи',
                'verbose_name': 'Група',
            },
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': 'Студенти', 'ordering': ['last_name'], 'verbose_name': 'Студент'},
        ),
        migrations.AlterField(
            model_name='student',
            name='ticket',
            field=models.CharField(verbose_name='Білет', max_length=256),
        ),
        migrations.AddField(
            model_name='group',
            name='leader',
            field=models.OneToOneField(on_delete=django.db.models.deletion.SET_NULL, to='students.Student', verbose_name='Староста', null=True, blank=True),
        ),
    ]
