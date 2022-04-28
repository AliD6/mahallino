# Generated by Django 4.0.3 on 2022-04-13 14:48

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlapp', '0004_alter_bus_updatedate'),
    ]

    operations = [
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
                ('geom', django.contrib.gis.db.models.fields.LineStringField(srid=32639)),
            ],
        ),
    ]