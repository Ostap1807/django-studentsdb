# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_exam_result'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam_result',
            options={'verbose_name': 'Результати іспиту', 'verbose_name_plural': 'Результати іспитів'},
        ),
    ]
