# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='anime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anime_title', models.CharField(max_length=63, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='sc_data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('anime_num', models.IntegerField()),
                ('img_data', models.ImageField(upload_to=b'', verbose_name=b'image')),
                ('created', models.DateField(auto_now_add=True)),
                ('ani_ti', models.ForeignKey(to='scsho.anime')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
