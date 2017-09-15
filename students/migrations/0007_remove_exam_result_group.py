# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20170915_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam_result',
            name='group',
        ),
    ]
