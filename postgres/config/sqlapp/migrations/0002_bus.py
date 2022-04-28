# Generated by Django 4.0.3 on 2022-04-13 14:22

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('stationcod', models.IntegerField()),
                ('linestatio', models.CharField(max_length=170, null=True)),
                ('linecount', models.IntegerField()),
                ('address', models.CharField(max_length=254, null=True)),
                ('direction', models.CharField(max_length=50, null=True)),
                ('sign', models.CharField(max_length=10, null=True)),
                ('marking', models.CharField(max_length=10, null=True)),
                ('color', models.CharField(max_length=10, null=True)),
                ('light', models.CharField(max_length=10, null=True)),
                ('seat', models.CharField(max_length=10, null=True)),
                ('shelter', models.CharField(max_length=10, null=True)),
                ('ticket', models.CharField(max_length=10, null=True)),
                ('monitor', models.CharField(max_length=10, null=True)),
                ('mapstop', models.CharField(max_length=10, null=True)),
                ('bridge', models.CharField(max_length=10, null=True)),
                ('attributes', models.CharField(max_length=10, null=True)),
                ('brt', models.CharField(max_length=10, null=True)),
                ('weight', models.CharField(max_length=10, null=True)),
                ('regionbus', models.CharField(max_length=30, null=True)),
                ('constructi', models.CharField(max_length=10, null=True)),
                ('laststand', models.CharField(max_length=10, null=True)),
                ('webkiosk', models.CharField(max_length=50, null=True)),
                ('timetable', models.CharField(max_length=10, null=True)),
                ('disabled', models.CharField(max_length=60, null=True)),
                ('project', models.CharField(max_length=80, null=True)),
                ('district', models.IntegerField()),
                ('subdistric', models.IntegerField()),
                ('layerid', models.CharField(max_length=20, null=True)),
                ('guid', models.CharField(max_length=38, null=True)),
                ('xutm', models.FloatField()),
                ('yutm', models.FloatField()),
                ('xgeo', models.FloatField()),
                ('ygeo', models.FloatField()),
                ('comment_field', models.CharField(max_length=254, null=True)),
                ('ttccid', models.BigIntegerField()),
                ('updateuser', models.CharField(max_length=150, null=True)),
                ('updatedate', models.DateField()),
                ('createduse', models.CharField(max_length=150, null=True)),
                ('createddat', models.DateField()),
                ('oddeven', models.CharField(max_length=70, null=True)),
                ('trafficzon', models.CharField(max_length=70, null=True)),
                ('disabledra', models.CharField(max_length=10, null=True)),
                ('braillesig', models.CharField(max_length=10, null=True)),
                ('blindspeci', models.CharField(max_length=10, null=True)),
                ('flexiblean', models.CharField(max_length=10, null=True)),
                ('braillegui', models.CharField(max_length=10, null=True)),
                ('stairtype', models.CharField(max_length=50, null=True)),
                ('gate', models.CharField(max_length=10, null=True)),
                ('reader', models.CharField(max_length=10, null=True)),
                ('stand', models.CharField(max_length=10, null=True)),
                ('transportm', models.CharField(max_length=70, null=True)),
                ('id_unique', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=32639)),
            ],
        ),
    ]
