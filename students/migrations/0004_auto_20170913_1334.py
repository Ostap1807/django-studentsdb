# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_student_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('subject', models.CharField(verbose_name='Назва предмету', max_length=256)),
                ('lecturer', models.CharField(verbose_name='Викладач', max_length=256)),
                ('date_of_exam', models.DateTimeField(verbose_name='Дата та час проведення')),
                ('notes', models.TextField(verbose_name='Додаткові нотатки', blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Іспит',
                'verbose_name_plural': 'Іспити',
            },
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Група', 'verbose_name_plural': 'Групи', 'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='exam',
            name='exams_group',
            field=models.ForeignKey(verbose_name='Група', to='students.Group'),
        ),
    ]
