# Generated by Django 4.0.3 on 2022-04-14 08:05

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bohran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.BigIntegerField()),
                ('name', models.CharField(max_length=254, null=True)),
                ('address', models.CharField(max_length=254, null=True)),
                ('explain', models.CharField(max_length=254, null=True)),
                ('priority', models.CharField(max_length=5, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=32639)),
            ],
        ),
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
                ('updatedate', models.DateField(blank=True, null=True)),
                ('createduse', models.CharField(max_length=150, null=True)),
                ('createddat', models.DateField(blank=True, null=True)),
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
        migrations.CreateModel(
            name='Busline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linenumber', models.BigIntegerField()),
                ('origin', models.CharField(max_length=60, null=True)),
                ('destinatio', models.CharField(max_length=60, null=True)),
                ('pathtype', models.CharField(max_length=12, null=True)),
                ('fare', models.BigIntegerField()),
                ('buscount', models.IntegerField()),
                ('servicetyp', models.CharField(max_length=20, null=True)),
                ('linetype', models.CharField(max_length=50, null=True)),
                ('splinedire', models.CharField(max_length=50, null=True)),
                ('splineleng', models.BigIntegerField()),
                ('controllin', models.CharField(max_length=10, null=True)),
                ('stationnum', models.BigIntegerField()),
                ('oldlinenum', models.CharField(max_length=15, null=True)),
                ('regionbus', models.IntegerField()),
                ('constructi', models.CharField(max_length=20, null=True)),
                ('ttccid', models.BigIntegerField()),
                ('workingtim', models.CharField(max_length=50, null=True)),
                ('moneycode', models.CharField(max_length=10, null=True)),
                ('beneficiar', models.BigIntegerField()),
                ('company', models.CharField(max_length=254, null=True)),
                ('district', models.CharField(max_length=30, null=True)),
                ('subdistric', models.IntegerField()),
                ('layerid', models.CharField(max_length=20, null=True)),
                ('guid_field', models.CharField(max_length=38, null=True)),
                ('comment_field', models.CharField(max_length=254, null=True)),
                ('speed', models.BigIntegerField()),
                ('updateuser', models.CharField(max_length=150, null=True)),
                ('updatedate', models.DateField(null=True)),
                ('createduse', models.CharField(max_length=150, null=True)),
                ('createddat', models.DateField(null=True)),
                ('oddeven', models.CharField(max_length=80, null=True)),
                ('trafficzon', models.CharField(max_length=70, null=True)),
                ('transportm', models.CharField(max_length=70, null=True)),
                ('shape_len', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(srid=32639)),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osm_id', models.CharField(max_length=10)),
                ('code', models.BigIntegerField()),
                ('fclass', models.CharField(max_length=28)),
                ('name', models.CharField(max_length=100, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
