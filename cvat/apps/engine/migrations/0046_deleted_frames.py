# Generated by Django 3.1.13 on 2021-12-15 13:10

import cvat.apps.engine.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0045_data_sorting_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='deleted_frames',
            field=cvat.apps.engine.models.IntArrayField(default=''),
        ),
    ]
