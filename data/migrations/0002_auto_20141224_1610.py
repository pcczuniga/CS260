# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.CharField(max_length=10, default='Pending'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
