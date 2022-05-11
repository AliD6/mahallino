from django.db import connection
import json
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Transport , Bohran , Bus , Busline  , Roads
# import wkt
import json


class PostConn():
    def __init__(self , lat , lon):
        self.lat = lat
        self.lon = lon
        self.pnt = Point(self.lon , self.lat , srid=4326)

    def db_conn(self):

        data  = []
        taxi = Transport.objects.annotate(distance=Distance('geom',self.pnt)).filter(fclass='taxi').order_by('distance')[:3]
        # taxi =  json.loads(serializers.serialize("json" ,taxi))[:3]
        # index = 1
        Taxi = []
        for item in taxi:
            Taxi.append({"dist" : item.distance.m , "name" : item.name , "lon" : item.geom.x , "lat" : item.geom.y})
            # index = index+1
        TAXI = {"title" : "TAXI" , "id" : "304" , "value" : Taxi }
        data.append(TAXI)

        metro = Transport.objects.annotate(distance=Distance('geom',self.pnt)).filter(fclass='railway_station').order_by('distance')[:3]
        # index = 1
        Metro = []
        for item in metro:
            Metro.append({"dist" : item.distance.m , "name" : item.name , "lon" : item.geom.x , "lat" : item.geom.y})
            # index = index+1
        METRO = {"title" : "METRO" , "id" : "301" , "value" : Metro }
        data.append(METRO)

        bohran = Bohran.objects.annotate(distance=Distance('geom' , self.pnt)).order_by('distance')[:3]
        # index = 1
        Bohran = {}
        for item in bohran:
            Bohran.append({"dist" : item.distance.m , "name" : item.name , "lon" : item.geom.x , "lat" : item.geom.y})
            # index = index + 1
        BOHRAN = {"title" : "BOHRAN" , "id" : "505" , "value" : Bohran}
        data.append(BOHRAN)

        bus = Bus.objects.annotate(distance=Distance('geom' , self.pnt)).order_by('distance')[:3]
        # index = 1
        Bus = {}
        for item in bus:
            Bus.append({"dist" : item.distance.m , "name" : item.name , "lon" : item.geom.x , "lat" : item.geom.y})
            # index = index +1
        BUS = {"title" : "BUS" , "id" : "303" , "value" : Bus}
        data.append(BUS)

        busline = Busline.objects.annotate(distance=Distance('geom' , self.pnt)).order_by('distance')[:3]
        # index = 1
        Busline = {}
        for item in busline:
            Busline.append({"dist" : item.distance.m , "source":item.origin , "destination": item.destinatio , "coor" : json.loads(item.geom.json) })
            # print(type(json.loads(item.geom.json)))
            # index = index + 1
        BUSLINE = {"title" : "BUSLINE" , "id" : "305" , "value" : Busline}
        data.append(BUSLINE)

        # roads = Roads.objects.annotate(distance=Distance('geom' , self.pnt)).order_by('distance')[:3]
        # index = 1
        # ROADS = {}
        # for item in roads:
        #     ROADS[str(index)] = {"dist" : item.distance.m  , "name" : item.name , "coor" : json.loads(item.geom.json) }
        #     # print(type(json.loads(item.geom.json)))
        #     index = index + 1

        return(data)
    


# 