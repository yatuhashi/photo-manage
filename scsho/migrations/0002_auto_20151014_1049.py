# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scsho', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sc_data',
            name='img_data',
            field=models.ImageField(upload_to=b'screen', verbose_name=b'image'),
        ),
    ]
