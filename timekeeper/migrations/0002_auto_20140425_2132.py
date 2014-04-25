# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'timekeeper', b'0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name=b'place',
            name=b'latitude',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name=b'place',
            name=b'longitude',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
