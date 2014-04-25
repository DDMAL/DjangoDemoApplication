# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name=b'Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'name', models.CharField(max_length=255, null=True, blank=True)),
                (b'latitude', models.FloatField()),
                (b'longitude', models.FloatField()),
                (b'created', models.DateTimeField(auto_now_add=True)),
                (b'updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name=b'Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'first_name', models.CharField(max_length=255, null=True, blank=True)),
                (b'last_name', models.CharField(max_length=255, null=True, blank=True)),
                (b'created', models.DateTimeField(auto_now_add=True)),
                (b'updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name=b'Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                (b'title', models.CharField(max_length=255, null=True, blank=True)),
                (b'start_time', models.DateTimeField()),
                (b'end_time', models.DateTimeField()),
                (b'created', models.DateTimeField(auto_now_add=True)),
                (b'updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
