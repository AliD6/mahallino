from django.db import connection
import json
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Transport , Bohran , Bus , Busline  , Roads , Hospital, Fire, Police, Pharmacy, School, Aludegi, Trafic, Busy, Park, Pool, Hotel, Zoo, Cng, Shop, Fuel, Gym, Mahalle, Mantaghe, Brt
# import wkt
import json
from django.core.serializers import serialize

class PostConn():
    def __init__(self , lat , lon):
        self.lat = lat
        self.lon = lon
        self.pnt = Point(self.lon , self.lat , srid=4326)

    def db_conn(self):

        # roads = Roads.objects.annotate(distance=Distance('geom' , self.pnt)).order_by('distance')[:3]
        # index = 1
        # ROADS = {}
        # for item in roads:
        #     ROADS[str(index)] = {"dist" : item.distance.m  , "name" : item.name , "coor" : json.loads(item.geom.json) }
        #     # print(type(json.loads(item.geom.json)))
        #     index = index + 1


        # aludegi_model = Aludegi.objects.annotate(distance=Distance('geom' , self.pnt)).order_by('distance')[:3]
        # aludegi_data = []
        # for item in aludegi_model:
        #     aludegi_data.append()

        return data

    def pertrans(self):
        data = []

        aludegi_model = Aludegi.objects.filter(geom__intersects=self.pnt)
        trafic_model = Trafic.objects.filter(geom__intersects=self.pnt)
        tarh = []
        tarh.append({"name" : "زوج و فرد" , "state" : bool(len(aludegi_model))})
        tarh.append({"name" : "آلودگی هوا" , "state" : bool(len(trafic_model))})
        TARH = {"title": "TARH", "id": 203, "value": tarh}
        data.append(TARH)

        busy_model = Busy.objects.annotate(distance=Distance('geom', self.pnt)).order_by('distance')
        busy_counter = 0
        for item in busy_model:
            if item.distance.m < 2000:
                busy_counter = busy_counter + 1
            else:
                break
        terafic = {"title": "terafic", "id": 201, "value": busy_counter}
        data.append(terafic)

        cng_model = Cng.objects.annotate(distance=Distance('geom', self.pnt)).order_by('distance')[:3]
        cng_data = []
        for item in cng_model:
            cng_data.append({"dist": item.distance.m, "name": item.name, "lon": item.geom.coords[0][0],
                             "lat": item.geom.coords[0][1]})
        CNG = {"title": "CNG", "id": 205, "value": cng_data}
        data.append(CNG)

        fuel_model = Fuel.objects.annotate(distance=Distance('geom', self.pnt)).order_by('distance')[:3]
        fuel_data = []
        for item in fuel_model:
            fuel_data.append({"dist": item.distance.m, "name": item.name, "lon": item.geom.coords[0][0],
                              "lat": item.geom.coords[0][1]})
        FUEL = {"title": "FUEL", "id": 204, "value": fuel_data}
        data.append(FUEL)

        return data

    def pubtrans(self):
        # Done Complete!
        data = []

        metro = Transport.objects.annotate(distance=Distance('geom', self.pnt)).filter(
            fclass='railway_station').order_by('distance')[:3]
        # index = 1
        MEtro = []
        for item in metro:
            MEtro.append({"dist": item.distance.m, "name": item.name, "lon": item.geom.x, "lat": item.geom.y})
            # index = index+1
        METRO = {"title": "METRO", "id": 301, "value": MEtro}
        data.append(METRO)

        bus = Bus.objects.annotate(distance=Distance('geom', self.pnt)).order_by('distance')[:3]
        # index = 1
        BUs = []
        for item in bus:
            BUs.append({"dist": item.distance.m, "name": item.name, "lon": item.geom.x, "lat": item.geom.y})
            # index = index +1
        BUS = {"title": "BUS", "id": 303, "value": BUs}
        data.append(BUS)

        busline = Busline.objects.annotate(distance=Distance('geom', self.pnt)).order_by('distance')[:3]
        # index = 1
        BUsline = []
        for item in busline:
            BUsline.append({"dist": item.distance.m, "source": item.origin, "destination": item.destinatio,
                            "coor": json.loads(item.geom.json)})
            # print(type(json.loads(item.geom.json)))
            # index = index + 1
        BUSLINE = {"title": "BUSLINE", "id": 305, "value": BUsline}
        data.append(BUSLINE)

        taxi = Transport.objects.annotate(distance=Distance('geom', self.pnt)).filter(fclass='taxi').order_by('distance')[:3]
        # taxi =  json.loads(serializers.serialize("json" ,taxi))[:3]
        # index = 1
        TAxi = []
        for item in taxi:
            TAxi.append({"dist": item.distance.m, "name": item.name, "lon": item.geom.x, "lat": item.geom.y})
            # index = index+1
        TAXI = {"title": "TAXI", "id": 304, "value": TAxi}
        data.append(TAXI)

        brt_model = Brt.objects.annotate(distance=Distance('geom', self.pnt)).order_by('distance')[:3]
        brt = []
        for item in brt_model:
            brt.append({"dist": item.distance.m, "name": item.name, "lon": item.geom.coords[0][0], "lat": item.geom.coords[0][1] , "line" : item.line})
        BRT = {"title": "BRT", "id": 302, "value": brt}
        data.append(BRT)

        return data

    def refahi(self):
        # cinema - cafe - restaurant left
        data = []
        gym_model = Gym.objects.annotate(distance=Distance('geom', self.pnt)).order_by('distance')[:3]
        gym_data = []
        for item in gym_model:
            gym_data.append({"dist": item.distance.m, "name": item.name, "lon": item.geom.coords[0][0],
                             "lat": item.geom.coords[0][1]})
        GYM = {"title": "GYM", "id": 405, "value": gym_data}
        data.append(GYM)

        pool_model = Pool.objects.annotate(distance=Distance('geom', self.pnt)).order_by('distance')[:3]
        pool_data = []
        for item in pool_model:
            pool_data.append({"dist": item.distance.m, "name": item.name, "lon": item.geom.coords[0][0],
                              "lat": item.geom.coords[0][1]})
        POOL = {"title": "POOL", "id": 406, "value": pool_data}
        data.append(POOL)

        shop_model = Shop.objects.annotate(distance=Distance('geom', self.pnt)).order_by('distance')[:3]
        shop_data = []
        for item in shop_model:
            shop_data.append({"dist": item.distance.m, "name": item.name, "lon": item.geom.coords[0][0],
                              "lat": item.geom.coords[0][1]})
        SHOP = {"title": "SHOP", "id": 407, "value": shop_data}
        data.append(SHOP)

        school_model = School.objects.annotate(distance=Distance('geom', self.pnt)).order_by('distance')[:3]
        school_data = []
        for item in school_model:
            school_data.append({"dist": item.distance.m, "name": item.name, "lon": item.geom.coords[0][0],
                                "lat": item.geom.coords[0][1]})
        SCHOOL = {"title": "SCHOOL", "id": 401, "value": school_data}
        data.append(SCHOOL)

        park_model = Park.objects.annotate(distance=Distance('geom', self.pnt)).order_by('distance')[:3]
        park_data = []
        for item in park_model:
            park_data.append({"dist": item.distance.m, "name": item.name, "lon": item.geom.coords[0][0],
                              "lat": item.geom.coords[0][1]})
        PARK = {"title": "PARK", "id": 403, "value": park_data}
        data.append(PARK)

        pharmacy_model = Pharmacy.objects.annotate(distance=Distance('geom', self.pnt)).order_by('distance')[:3]
        pharmacy_data = []
        for item in pharmacy_model:
            pharmacy_data.append({"dist": item.distance.m, "name": item.name, "lon": item.geom.coords[0][0],
                                  "lat": item.geom.coords[0][1]})
        PHARMACY = {"title": "PHARMACY", "id": 404, "value": pharmacy_data}
        data.append(PHARMACY)

        hotel_model = Hotel.objects.annotate(distance=Distance('geom', self.pnt)).order_by('distance')[:3]
        hotel_data = []
        for item in hotel_model:
            hotel_data.append({"dist": item.distance.m, "name": item.name, "lon": item.geom.coords[0][0],
                               "lat": item.geom.coords[0][1]})
        HOTEL = {"title": "HOTEL", "id": 409, "value": hotel_data}
        data.append(HOTEL)

        zoo_model = Zoo.objects.annotate(distance=Distance('geom', self.pnt)).order_by('distance')[:3]
        zoo_data = []
        for item in zoo_model:
            zoo_data.append({"dist": item.distance.m, "name": item.name, "lon": item.geom.coords[0][0],
                             "lat": item.geom.coords[0][1]})
        ZOO = {"title": "ZOO", "id": 410, "value": zoo_data}
        data.append(ZOO)

        return data

    def security(self):
        # Done Completed!
        data = []

        fire_model = Fire.objects.annotate(distance=Distance('geom', self.pnt)).order_by('distance')[:3]
        fire_data = []
        for item in fire_model:
            fire_data.append({"dist": item.distance.m, "name": item.name, "lon": item.geom.coords[0][0],
                              "lat": item.geom.coords[0][1]})
        FIRE = {"title": "FIRE", "id": 502, "value": fire_data}
        data.append(FIRE)

        police_model = Police.objects.annotate(distance=Distance('geom', self.pnt)).order_by('distance')[:3]
        police_data = []
        for item in police_model:
            police_data.append({"dist": item.distance.m, "name": item.name, "lon": item.geom.coords[0][0],
                                "lat": item.geom.coords[0][1]})
        POLICE = {"title": "POLICE", "id": 501, "value": police_data}
        data.append(POLICE)

        hospital_model = Hospital.objects.annotate(distance=Distance('geom', self.pnt)).order_by('distance')[:3]
        hospital_data = []
        for item in hospital_model:
            hospital_data.append({"dist": item.distance.m, "name": item.name, "lon": item.geom.coords[0][0],
                                  "lat": item.geom.coords[0][1]})
        HOSPITAL = {"title": "HOSPITAL", "id": 503, "value": hospital_data}
        data.append(HOSPITAL)

        bohran = Bohran.objects.annotate(distance=Distance('geom', self.pnt)).order_by('distance')[:3]
        # index = 1
        BOhran = []
        for item in bohran:
            BOhran.append({"dist": item.distance.m, "name": item.name, "lon": item.geom.x, "lat": item.geom.y})
            # index = index + 1
        BOHRAN = {"title": "BOHRAN", "id": 505, "value": BOhran}
        data.append(BOHRAN)

        return data