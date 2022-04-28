from django.db import connection
import json
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Transport , Bohran , Bus , Busline
# import wkt
import json


class PostConn():
    def __init__(self , lat , lon):
        self.lat = lat
        self.lon = lon
        self.pnt = Point(self.lon , self.lat , srid=4326)

    def db_conn(self):
        taxi = Transport.objects.annotate(distance=Distance('geom',self.pnt)).filter(fclass='taxi').order_by('distance')[:3]
        # taxi =  json.loads(serializers.serialize("json" ,taxi))[:3]
        index = 1
        TAXI = {}
        for item in taxi:
            TAXI[str(index)] = {"dist" : item.distance.m , "name" : item.name , "lon" : item.geom.x , "lat" : item.geom.y}
            index = index+1

        
        metro = Transport.objects.annotate(distance=Distance('geom',self.pnt)).filter(fclass='railway_station').order_by('distance')[:3]
        index = 1
        METRO = {}
        for item in metro:
            METRO[str(index)] = {"dist" : item.distance.m , "name" : item.name , "lon" : item.geom.x , "lat" : item.geom.y}
            index = index+1

        bohran = Bohran.objects.annotate(distance=Distance('geom' , self.pnt)).order_by('distance')[:3]
        index = 1
        BOHRAN = {}
        for item in bohran:
            BOHRAN[str(index)] = {"dist" : item.distance.m , "name" : item.name , "lon" : item.geom.x , "lat" : item.geom.y}
            index = index + 1
        
        bus = Bus.objects.annotate(distance=Distance('geom' , self.pnt)).order_by('distance')[:3]
        index = 1
        BUS = {}
        for item in bus:
            BUS[str(index)] = {"dist" : item.distance.m , "name" : item.name , "lon" : item.geom.x , "lat" : item.geom.y}
            index = index +1

        busline = Busline.objects.annotate(distance=Distance('geom' , self.pnt)).order_by('distance')[:3]
        index = 1
        BUSLINE = {}
        for item in busline:
            BUSLINE[str(index)] = {"dist" : item.distance.m , "source":item.origin , "destination": item.destinatio , "coor" : json.loads(item.geom.json) }
            print(type(json.loads(item.geom.json)))
            index = index + 1


        

        return({"status" : "200" , "message" : "done" , "taxi" : TAXI , "metro": METRO , "BOHRAN" : BOHRAN , "BUS" : BUS , "BUSLINE" : BUSLINE})
    


# 