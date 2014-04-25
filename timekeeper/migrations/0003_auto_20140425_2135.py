# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'timekeeper', b'0002_auto_20140425_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name=b'activity',
            name=b'place',
            field=models.ForeignKey(to=b'timekeeper.Place', default=1, to_field='id'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name=b'activity',
            name=b'partner',
            field=models.ForeignKey(to_field='id', blank=True, to=b'timekeeper.Person', null=True),
            preserve_default=True,
        ),
    ]
