# from django.db import models

# # Create your models here.

from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User , on_delete=models.SET_NULL , null=True)
    title = models.CharField(max_length=50 , null=True)
    id = models.CharField(primary_key=True , max_length=16)
    location = models.PointField(null=True)
    # created_at = models.DateTimeField(default=now)


class Transport(models.Model):
    osm_id = models.CharField(max_length=10)
    code = models.BigIntegerField()
    fclass = models.CharField(max_length=28)
    name = models.CharField(max_length=100,null=True)
    geom = models.PointField()



class Bohran(models.Model):
    objectid = models.BigIntegerField()
    name = models.CharField(max_length=254 , null=True)
    address = models.CharField(max_length=254 , null=True)
    explain = models.CharField(max_length=254 , null=True)
    priority = models.CharField(max_length=5 , null=True)
    geom = models.PointField(srid=4326)



class Bus(models.Model):
    name = models.CharField(max_length=150,null=True)
    stationcod = models.IntegerField()
    linestatio = models.CharField(max_length=170,null=True)
    linecount = models.IntegerField()
    address = models.CharField(max_length=254,null=True)
    direction = models.CharField(max_length=50,null=True)
    sign = models.CharField(max_length=10,null=True)
    marking = models.CharField(max_length=10,null=True)
    color = models.CharField(max_length=10,null=True)
    light = models.CharField(max_length=10,null=True)
    seat = models.CharField(max_length=10,null=True)
    shelter = models.CharField(max_length=10,null=True)
    ticket = models.CharField(max_length=10,null=True)
    monitor = models.CharField(max_length=10,null=True)
    mapstop = models.CharField(max_length=10,null=True)
    bridge = models.CharField(max_length=10,null=True)
    attributes = models.CharField(max_length=10,null=True)
    brt = models.CharField(max_length=10,null=True)
    weight = models.CharField(max_length=10,null=True)
    regionbus = models.CharField(max_length=30,null=True)
    constructi = models.CharField(max_length=10,null=True)
    laststand = models.CharField(max_length=10,null=True)
    webkiosk = models.CharField(max_length=50,null=True)
    timetable = models.CharField(max_length=10,null=True)
    disabled = models.CharField(max_length=60,null=True)
    project = models.CharField(max_length=80,null=True)
    district = models.IntegerField()
    subdistric = models.IntegerField()
    layerid = models.CharField(max_length=20,null=True)
    guid = models.CharField(max_length=38,null=True)
    xutm = models.FloatField()
    yutm = models.FloatField()
    xgeo = models.FloatField()
    ygeo = models.FloatField()
    comment_field = models.CharField(max_length=254,null=True)
    ttccid = models.BigIntegerField()
    updateuser = models.CharField(max_length=150,null=True)
    updatedate = models.DateField(null=True, blank=True)
    createduse = models.CharField(max_length=150,null=True)
    createddat = models.DateField(null=True, blank=True)
    oddeven = models.CharField(max_length=70,null=True)
    trafficzon = models.CharField(max_length=70,null=True)
    disabledra = models.CharField(max_length=10,null=True)
    braillesig = models.CharField(max_length=10,null=True)
    blindspeci = models.CharField(max_length=10,null=True)
    flexiblean = models.CharField(max_length=10,null=True)
    braillegui = models.CharField(max_length=10,null=True)
    stairtype = models.CharField(max_length=50,null=True)
    gate = models.CharField(max_length=10,null=True)
    reader = models.CharField(max_length=10,null=True)
    stand = models.CharField(max_length=10,null=True)
    transportm = models.CharField(max_length=70,null=True)
    id_unique = models.FloatField()
    geom = models.PointField(srid=4326)


class Busline(models.Model):
    linenumber = models.BigIntegerField()
    origin = models.CharField(max_length=60,null=True)
    destinatio = models.CharField(max_length=60,null=True)
    pathtype = models.CharField(max_length=12,null=True)
    fare = models.BigIntegerField()
    buscount = models.IntegerField()
    servicetyp = models.CharField(max_length=20,null=True)
    linetype = models.CharField(max_length=50,null=True)
    splinedire = models.CharField(max_length=50,null=True)
    splineleng = models.BigIntegerField()
    controllin = models.CharField(max_length=10,null=True)
    stationnum = models.BigIntegerField()
    oldlinenum = models.CharField(max_length=15,null=True)
    regionbus = models.IntegerField()
    constructi = models.CharField(max_length=20,null=True)
    ttccid = models.BigIntegerField()
    workingtim = models.CharField(max_length=50,null=True)
    moneycode = models.CharField(max_length=10,null=True)
    beneficiar = models.BigIntegerField()
    company = models.CharField(max_length=254,null=True)
    district = models.CharField(max_length=30,null=True)
    subdistric = models.IntegerField()
    layerid = models.CharField(max_length=20,null=True)
    guid_field = models.CharField(max_length=38,null=True)
    comment_field = models.CharField(max_length=254,null=True)
    speed = models.BigIntegerField()
    updateuser = models.CharField(max_length=150,null=True)
    updatedate = models.DateField(null=True)
    createduse = models.CharField(max_length=150,null=True)
    createddat = models.DateField(null=True)
    oddeven = models.CharField(max_length=80,null=True)
    trafficzon = models.CharField(max_length=70,null=True)
    transportm = models.CharField(max_length=70,null=True)
    shape_len = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)




class Roads(models.Model):
    entity = models.CharField(max_length=14,null=True)
    mslink_dmr = models.FloatField()
    fname = models.CharField(max_length=32,null=True)
    mapid = models.BigIntegerField()
    name = models.CharField(max_length=30,null=True)
    width = models.FloatField()
    bound = models.BigIntegerField()
    operation_field = models.CharField(max_length=17,null=True)
    recno = models.BigIntegerField()
    geom = models.MultiLineStringField(srid=32639)


class Hospital(models.Model):
    objectid_1 = models.BigIntegerField()
    objectid = models.BigIntegerField()
    fid_medica = models.BigIntegerField()
    entity = models.CharField(max_length=14,null=True)
    mslink_dmr = models.FloatField()
    fname = models.CharField(max_length=32,null=True)
    mapid = models.BigIntegerField()
    name = models.CharField(max_length=37,null=True)
    kind = models.CharField(max_length=33,null=True)
    capacity = models.BigIntegerField()
    operation_field = models.CharField(max_length=17,null=True)
    recno = models.BigIntegerField()
    fid_medi_1 = models.BigIntegerField()
    entity_1 = models.CharField(max_length=14,null=True)
    mslink_d_1 = models.FloatField()
    fname_1 = models.CharField(max_length=32,null=True)
    mapid_1 = models.BigIntegerField()
    name_1 = models.CharField(max_length=33,null=True)
    kind_1 = models.CharField(max_length=11,null=True)
    capacity_1 = models.BigIntegerField()
    operation1 = models.CharField(max_length=17,null=True)
    recno_1 = models.BigIntegerField()
    fid_hospit = models.BigIntegerField()
    osm_id = models.CharField(max_length=10,null=True)
    code = models.BigIntegerField()
    fclass = models.CharField(max_length=28,null=True)
    name_12 = models.CharField(max_length=100,null=True)
    shape_leng = models.FloatField()
    orig_fid = models.BigIntegerField()
    geom = models.MultiPointField(srid=4326)


class Fire(models.Model):
    fclass = models.CharField(max_length=28,null=True)
    name = models.CharField(max_length=100,null=True)
    geom = models.MultiPointField(srid=4326)


class Police(models.Model):
    osm_id = models.CharField(max_length=10,null=True)
    code = models.BigIntegerField()
    fclass = models.CharField(max_length=28,null=True)
    name = models.CharField(max_length=100,null=True)
    geom = models.MultiPointField(srid=4326)


class Pharmacy(models.Model):
    osm_id = models.CharField(max_length=10,null=True)
    code = models.BigIntegerField()
    fclass = models.CharField(max_length=28,null=True)
    name = models.CharField(max_length=100,null=True)
    geom = models.MultiPointField(srid=4326)

class School(models.Model):
    code = models.BigIntegerField()
    fclass = models.CharField(max_length=28,null=True)
    name = models.CharField(max_length=100,null=True)
    orig_fid = models.BigIntegerField()
    geom = models.MultiPointField(srid=4326)

class Aludegi(models.Model):
    name = models.CharField(max_length=80,null=True)
    descriptio = models.CharField(max_length=253,null=True)
    geom = models.MultiPolygonField(srid=4326)

class Trafic(models.Model):
    name = models.CharField(max_length=80,null=True)
    descriptio = models.CharField(max_length=254,null=True)
    geom = models.MultiPolygonField(srid=4326)

class Busy(models.Model):
    osm_id = models.CharField(max_length=10,null=True)
    code = models.BigIntegerField()
    fclass = models.CharField(max_length=28,null=True)
    name = models.CharField(max_length=100,null=True)
    geom = models.MultiPointField(srid=4326)


class Park(models.Model):
    objectid_1 = models.BigIntegerField()
    name = models.CharField(max_length=100,null=True)
    objectid = models.BigIntegerField()
    code = models.BigIntegerField()
    fclass = models.CharField(max_length=28,null=True)
    orig_fid = models.BigIntegerField()
    geom = models.MultiPointField(srid=4326)


class Pool(models.Model):
    objectid = models.BigIntegerField()
    code = models.BigIntegerField()
    fclass = models.CharField(max_length=28,null=True)
    name = models.CharField(max_length=100,null=True)
    orig_fid = models.BigIntegerField()
    geom = models.MultiPointField(srid=4326)


class Hotel(models.Model):
    osm_id = models.CharField(max_length=254,null=True)
    name = models.CharField(max_length=254,null=True)
    barrier = models.CharField(max_length=254,null=True)
    highway = models.CharField(max_length=254,null=True)
    ref = models.CharField(max_length=254,null=True)
    address = models.CharField(max_length=254,null=True)
    is_in = models.CharField(max_length=254,null=True)
    place = models.CharField(max_length=254,null=True)
    man_made = models.CharField(max_length=254,null=True)
    other_tags = models.CharField(max_length=254,null=True)
    geom = models.MultiPointField(srid=4326)


class Zoo(models.Model):
    osm_id = models.CharField(max_length=254,null=True)
    name = models.CharField(max_length=254,null=True)
    barrier = models.CharField(max_length=254,null=True)
    highway = models.CharField(max_length=254,null=True)
    ref = models.CharField(max_length=254,null=True)
    address = models.CharField(max_length=254,null=True)
    is_in = models.CharField(max_length=254,null=True)
    place = models.CharField(max_length=254,null=True)
    man_made = models.CharField(max_length=254,null=True)
    other_tags = models.CharField(max_length=254,null=True)
    geom = models.MultiPointField(srid=4326)


class Cng(models.Model):
    osm_id = models.CharField(max_length=254,null=True)
    name = models.CharField(max_length=254,null=True)
    barrier = models.CharField(max_length=254,null=True)
    highway = models.CharField(max_length=254,null=True)
    ref = models.CharField(max_length=254,null=True)
    address = models.CharField(max_length=254,null=True)
    is_in = models.CharField(max_length=254,null=True)
    place = models.CharField(max_length=254,null=True)
    man_made = models.CharField(max_length=254,null=True)
    other_tags = models.CharField(max_length=254,null=True)
    geom = models.MultiPointField(srid=4326)


class Shop(models.Model):
    osm_id = models.CharField(max_length=254,null=True)
    name = models.CharField(max_length=254,null=True)
    barrier = models.CharField(max_length=254,null=True)
    highway = models.CharField(max_length=254,null=True)
    ref = models.CharField(max_length=254,null=True)
    address = models.CharField(max_length=254,null=True)
    is_in = models.CharField(max_length=254,null=True)
    place = models.CharField(max_length=254,null=True)
    man_made = models.CharField(max_length=254,null=True)
    other_tags = models.CharField(max_length=254,null=True)
    geom = models.MultiPointField(srid=4326)


class Fuel(models.Model):
    osm_id = models.CharField(max_length=254,null=True)
    name = models.CharField(max_length=254,null=True)
    barrier = models.CharField(max_length=254,null=True)
    highway = models.CharField(max_length=254,null=True)
    ref = models.CharField(max_length=254,null=True)
    address = models.CharField(max_length=254,null=True)
    is_in = models.CharField(max_length=254,null=True)
    place = models.CharField(max_length=254,null=True)
    man_made = models.CharField(max_length=254,null=True)
    other_tags = models.CharField(max_length=254,null=True)
    geom = models.MultiPointField(srid=4326)


class Gym(models.Model):
    osm_id = models.CharField(max_length=254,null=True)
    name = models.CharField(max_length=254,null=True)
    barrier = models.CharField(max_length=254,null=True)
    highway = models.CharField(max_length=254,null=True)
    ref = models.CharField(max_length=254,null=True)
    address = models.CharField(max_length=254,null=True)
    is_in = models.CharField(max_length=254,null=True)
    place = models.CharField(max_length=254,null=True)
    man_made = models.CharField(max_length=254,null=True)
    other_tags = models.CharField(max_length=254,null=True)
    geom = models.MultiPointField(srid=4326)


class Mahalle(models.Model):
    objectid_1 = models.BigIntegerField()
    region = models.BigIntegerField()
    nahiye = models.FloatField()
    pop85 = models.FloatField()
    pop85_zan = models.FloatField()
    pop85_mard = models.FloatField()
    khanvar = models.FloatField()
    mahale_nam = models.CharField(max_length=254,null=True)
    mahale_cod = models.FloatField()
    pop90_kol = models.FloatField()
    pop90_zan = models.FloatField()
    pop90_mard = models.FloatField()
    tedad90_kh = models.FloatField()
    basavad_ko = models.FloatField()
    basavad_ma = models.FloatField()
    basavad_za = models.FloatField()
    bisavad_ko = models.FloatField()
    bisavad_ma = models.FloatField()
    bisavad_za = models.FloatField()
    bishaz10sa = models.FloatField()
    bishaz10_1 = models.FloatField()
    bishaz10_2 = models.FloatField()
    mohajeran_field = models.FloatField()
    mohajeran1 = models.FloatField()
    mohajera_1 = models.FloatField()
    shaghelan_field = models.FloatField()
    bikaran_bi = models.FloatField()
    shaghelan1 = models.FloatField()
    bikaran_1 = models.FloatField()
    shaghela_1 = models.FloatField()
    bikaran_2 = models.FloatField()
    pop_malul_field = models.FloatField()
    pop_malul1 = models.FloatField()
    pop_malu_1 = models.FloatField()
    masahat_ma = models.FloatField()
    tarakom_ja = models.FloatField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    pop95_kol = models.BigIntegerField()
    pop95_zan = models.BigIntegerField()
    pop95_mard = models.BigIntegerField()
    geom = models.MultiPolygonField(srid=4326)


class Mantaghe(models.Model):
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    mantagheh = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)


class Brt(models.Model):
    osm_id = models.CharField(max_length=10,null=True)
    code = models.BigIntegerField()
    fclass = models.CharField(max_length=28,null=True)
    name = models.CharField(max_length=100,null=True)
    line = models.CharField(max_length=2 , null=True , blank=True)
    geom = models.MultiPointField(srid=4326)
