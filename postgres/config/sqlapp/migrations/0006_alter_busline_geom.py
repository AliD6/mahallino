# Generated by Django 4.0.3 on 2022-04-13 14:50

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sqlapp', '0005_busline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busline',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiLineStringField(srid=32639),
        ),
    ]
