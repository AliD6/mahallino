from .models import Transport , Bohran , Bus , Busline , Roads , Hospital, Fire, Police, Pharmacy, School, Aludegi, Trafic, Busy, Park, Pool, Hotel, Zoo, Cng, Shop, Fuel, Gym, Mahalle, Mantaghe, Brt
from django.contrib.gis.utils import LayerMapping
from pathlib import Path
from utils import LayerAdd


# # Auto-generated `LayerMapping` dictionary for Transport model
transport_mapping = {
    'osm_id': 'osm_id',
    'code': 'code',
    'fclass': 'fclass',
    'name': 'name',
    'geom': 'POINT',
}

transport_shp  = Path(__file__).resolve().parent / 'data' / 'Transport_Station.shp'





# Auto-generated `LayerMapping` dictionary for Bohran model
bohran_mapping = {
    'objectid': 'OBJECTID',
    'name': 'NAME',
    'address': 'ADDRESS',
    'explain': 'EXPLAIN',
    'priority': 'PRIORITY',
    'geom': 'POINT',
}

bohran_shp  = Path(__file__).resolve().parent / 'data' / 'BOHRAN' / 'BOHRAN.shp'


# Auto-generated `LayerMapping` dictionary for bus model
bus_mapping = {
    'name': 'NAME',
    'stationcod': 'STATIONCOD',
    'linestatio': 'LINESTATIO',
    'linecount': 'LINECOUNT',
    'address': 'ADDRESS',
    'direction': 'DIRECTION',
    'sign': 'SIGN',
    'marking': 'MARKING',
    'color': 'COLOR',
    'light': 'LIGHT',
    'seat': 'SEAT',
    'shelter': 'SHELTER',
    'ticket': 'TICKET',
    'monitor': 'MONITOR',
    'mapstop': 'MAPSTOP',
    'bridge': 'BRIDGE',
    'attributes': 'ATTRIBUTES',
    'brt': 'BRT',
    'weight': 'WEIGHT',
    'regionbus': 'REGIONBUS',
    'constructi': 'CONSTRUCTI',
    'laststand': 'LASTSTAND',
    'webkiosk': 'WEBKIOSK',
    'timetable': 'TIMETABLE',
    'disabled': 'DISABLED',
    'project': 'PROJECT',
    'district': 'DISTRICT',
    'subdistric': 'SUBDISTRIC',
    'layerid': 'LAYERID',
    'guid': 'GUID',
    'xutm': 'XUTM',
    'yutm': 'YUTM',
    'xgeo': 'XGEO',
    'ygeo': 'YGEO',
    'comment_field': 'COMMENT_',
    'ttccid': 'TTCCID',
    'updateuser': 'UPDATEUSER',
    'updatedate': 'UPDATEDATE',
    'createduse': 'CREATEDUSE',
    'createddat': 'CREATEDDAT',
    'oddeven': 'ODDEVEN',
    'trafficzon': 'TRAFFICZON',
    'disabledra': 'DISABLEDRA',
    'braillesig': 'BRAILLESIG',
    'blindspeci': 'BLINDSPECI',
    'flexiblean': 'FLEXIBLEAN',
    'braillegui': 'BRAILLEGUI',
    'stairtype': 'STAIRTYPE',
    'gate': 'GATE',
    'reader': 'READER',
    'stand': 'STAND',
    'transportm': 'TRANSPORTM',
    'id_unique': 'ID_UNIQUE',
    'geom': 'POINT',
}

bus_shp  = Path(__file__).resolve().parent / 'data' / 'BUS' / 'BUS.shp'

# Auto-generated `LayerMapping` dictionary for busline model
busline_mapping = {
    'linenumber': 'LINENUMBER',
    'origin': 'ORIGIN',
    'destinatio': 'DESTINATIO',
    'pathtype': 'PATHTYPE',
    'fare': 'FARE',
    'buscount': 'BUSCOUNT',
    'servicetyp': 'SERVICETYP',
    'linetype': 'LINETYPE',
    'splinedire': 'SPLINEDIRE',
    'splineleng': 'SPLINELENG',
    'controllin': 'CONTROLLIN',
    'stationnum': 'STATIONNUM',
    'oldlinenum': 'OLDLINENUM',
    'regionbus': 'REGIONBUS',
    'constructi': 'CONSTRUCTI',
    'ttccid': 'TTCCID',
    'workingtim': 'WORKINGTIM',
    'moneycode': 'MONEYCODE',
    'beneficiar': 'BENEFICIAR',
    'company': 'COMPANY',
    'district': 'DISTRICT',
    'subdistric': 'SUBDISTRIC',
    'layerid': 'LAYERID',
    'guid_field': 'GUID_',
    'comment_field': 'COMMENT_',
    'speed': 'SPEED',
    'updateuser': 'UPDATEUSER',
    'updatedate': 'UPDATEDATE',
    'createduse': 'CREATEDUSE',
    'createddat': 'CREATEDDAT',
    'oddeven': 'ODDEVEN',
    'trafficzon': 'TRAFFICZON',
    'transportm': 'TRANSPORTM',
    'shape_len': 'SHAPE_LEN',
    'geom': 'LINESTRING',
}

busline_shp  = Path(__file__).resolve().parent / 'data' / 'busline' / 'busline.shp'

# Auto-generated `LayerMapping` dictionary for roads model
roads_mapping = {
    'entity': 'ENTITY',
    'mslink_dmr': 'MSLINK_DMR',
    'fname': 'FNAME',
    'mapid': 'MAPID',
    'name': 'NAME',
    'width': 'WIDTH',
    'bound': 'BOUND',
    'operation_field': 'OPERATION_',
    'recno': 'RECNO',
    'geom': 'LINESTRING',
}

roads_shp  = Path(__file__).resolve().parent / 'data' / 'roads' / 'high.shp'

hospital_mapping = {
    'objectid_1': 'OBJECTID_1',
    'objectid': 'OBJECTID',
    'fid_medica': 'FID_Medica',
    'entity': 'ENTITY',
    'mslink_dmr': 'MSLINK_DMR',
    'fname': 'FNAME',
    'mapid': 'MAPID',
    'name': 'NAME',
    'kind': 'KIND',
    'capacity': 'CAPACITY',
    'operation_field': 'OPERATION_',
    'recno': 'RECNO',
    'fid_medi_1': 'FID_Medi_1',
    'entity_1': 'ENTITY_1',
    'mslink_d_1': 'MSLINK_D_1',
    'fname_1': 'FNAME_1',
    'mapid_1': 'MAPID_1',
    'name_1': 'NAME_1',
    'kind_1': 'KIND_1',
    'capacity_1': 'CAPACITY_1',
    'operation1': 'OPERATION1',
    'recno_1': 'RECNO_1',
    'fid_hospit': 'FID_Hospit',
    'osm_id': 'osm_id',
    'code': 'code',
    'fclass': 'fclass',
    'name_12': 'name_12',
    'shape_leng': 'Shape_Leng',
    'orig_fid': 'ORIG_FID',
    'geom': 'MULTIPOINT',
}

hospital_shp  = Path(__file__).resolve().parent / 'data' / 'hospital' / 'Medical_Centers.shp'

fire_mapping = {
    'fclass': 'fclass',
    'name': 'name',
    'geom': 'MULTIPOINT',
}
fire_shp  = Path(__file__).resolve().parent / 'data' / 'fire' / 'Fire_Stations.shp'

police_mapping = {
    'osm_id': 'osm_id',
    'code': 'code',
    'fclass': 'fclass',
    'name': 'name',
    'geom': 'MULTIPOINT',
}

police_shp  = Path(__file__).resolve().parent / 'data' / 'police' / 'Police_Stations.shp'

pharmacy_mapping = {
    'osm_id': 'osm_id',
    'code': 'code',
    'fclass': 'fclass',
    'name': 'name',
    'geom': 'MULTIPOINT',
}

pharmacy_shp  = Path(__file__).resolve().parent / 'data' / 'pharmacy' / 'Pharmacy.shp'

school_mapping = {
    'code': 'code',
    'fclass': 'fclass',
    'name': 'name',
    'orig_fid': 'ORIG_FID',
    'geom': 'MULTIPOINT',
}

school_shp  = Path(__file__).resolve().parent / 'data' / 'school' / 'school.shp'



aludegi_mapping = {
    'name': 'Name',
    'descriptio': 'descriptio',
    'geom': 'MULTIPOLYGON',
}

aludegi_shp  = Path(__file__).resolve().parent / 'data' / 'aludegi' / '--_-_--polygon.shp'

trafic_mapping = {
    'name': 'Name',
    'descriptio': 'descriptio',
    'geom': 'MULTIPOLYGON',
}
trafic_shp  = Path(__file__).resolve().parent / 'data' / 'trafic' / '-_--polygon.shp'

busy_mapping = {
    'osm_id': 'osm_id',
    'code': 'code',
    'fclass': 'fclass',
    'name': 'name',
    'geom': 'MULTIPOINT',
}
busy_shp  = Path(__file__).resolve().parent / 'data' / 'busy' / 'Traffic.shp'


park_mapping = {
    'objectid_1': 'OBJECTID_1',
    'name': 'name',
    'objectid': 'OBJECTID',
    'code': 'code',
    'fclass': 'fclass',
    'orig_fid': 'ORIG_FID',
    'geom': 'MULTIPOINT',
}
park_shp  = Path(__file__).resolve().parent / 'data' / 'park' / 'park.shp'

pool_mapping = {
    'objectid': 'OBJECTID',
    'code': 'code',
    'fclass': 'fclass',
    'name': 'name',
    'orig_fid': 'ORIG_FID',
    'geom': 'MULTIPOINT',
}
pool_shp  = Path(__file__).resolve().parent / 'data' / 'pool' / 'pool.shp'

hotel_mapping = {
    'osm_id': 'osm_id',
    'name': 'name',
    'barrier': 'barrier',
    'highway': 'highway',
    'ref': 'ref',
    'address': 'address',
    'is_in': 'is_in',
    'place': 'place',
    'man_made': 'man_made',
    'other_tags': 'other_tags',
    'geom': 'MULTIPOINT',
}
hotel_shp  = Path(__file__).resolve().parent / 'data' / 'hotel' / 'hotel.shp'

zoo_mapping = {
    'osm_id': 'osm_id',
    'name': 'name',
    'barrier': 'barrier',
    'highway': 'highway',
    'ref': 'ref',
    'address': 'address',
    'is_in': 'is_in',
    'place': 'place',
    'man_made': 'man_made',
    'other_tags': 'other_tags',
    'geom': 'MULTIPOINT',
}
zoo_shp  = Path(__file__).resolve().parent / 'data' / 'zoo' / 'zoo.shp'

cng_mapping = {
    'osm_id': 'osm_id',
    'name': 'name',
    'barrier': 'barrier',
    'highway': 'highway',
    'ref': 'ref',
    'address': 'address',
    'is_in': 'is_in',
    'place': 'place',
    'man_made': 'man_made',
    'other_tags': 'other_tags',
    'geom': 'MULTIPOINT',
}
cng_shp  = Path(__file__).resolve().parent / 'data' / 'cng' / 'CNG.shp'

shop_mapping = {
    'osm_id': 'osm_id',
    'name': 'name',
    'barrier': 'barrier',
    'highway': 'highway',
    'ref': 'ref',
    'address': 'address',
    'is_in': 'is_in',
    'place': 'place',
    'man_made': 'man_made',
    'other_tags': 'other_tags',
    'geom': 'MULTIPOINT',
}
shop_shp  = Path(__file__).resolve().parent / 'data' / 'shop' / 'supermarket.shp'

fuel_mapping = {
    'osm_id': 'osm_id',
    'name': 'name',
    'barrier': 'barrier',
    'highway': 'highway',
    'ref': 'ref',
    'address': 'address',
    'is_in': 'is_in',
    'place': 'place',
    'man_made': 'man_made',
    'other_tags': 'other_tags',
    'geom': 'MULTIPOINT',
}
fuel_shp  = Path(__file__).resolve().parent / 'data' / 'fuel' / 'fuel.shp'

gym_mapping = {
    'osm_id': 'osm_id',
    'name': 'name',
    'barrier': 'barrier',
    'highway': 'highway',
    'ref': 'ref',
    'address': 'address',
    'is_in': 'is_in',
    'place': 'place',
    'man_made': 'man_made',
    'other_tags': 'other_tags',
    'geom': 'MULTIPOINT',
}
gym_shp  = Path(__file__).resolve().parent / 'data' / 'gym' / 'gyms2.shp'

mahalle_mapping = {
    'objectid_1': 'OBJECTID_1',
    'region': 'Region',
    'nahiye': 'Nahiye',
    'pop85': 'Pop85',
    'pop85_zan': 'Pop85_Zan',
    'pop85_mard': 'Pop85_Mard',
    'khanvar': 'Khanvar',
    'mahale_nam': 'Mahale_nam',
    'mahale_cod': 'Mahale_cod',
    'pop90_kol': 'Pop90_kol',
    'pop90_zan': 'Pop90_zan',
    'pop90_mard': 'Pop90_mard',
    'tedad90_kh': 'Tedad90_kh',
    'basavad_ko': 'Basavad_ko',
    'basavad_ma': 'Basavad_ma',
    'basavad_za': 'Basavad_za',
    'bisavad_ko': 'Bisavad_ko',
    'bisavad_ma': 'Bisavad_ma',
    'bisavad_za': 'Bisavad_za',
    'bishaz10sa': 'Bishaz10sa',
    'bishaz10_1': 'Bishaz10_1',
    'bishaz10_2': 'Bishaz10_2',
    'mohajeran_field': 'Mohajeran_',
    'mohajeran1': 'Mohajeran1',
    'mohajera_1': 'Mohajera_1',
    'shaghelan_field': 'Shaghelan_',
    'bikaran_bi': 'Bikaran_bi',
    'shaghelan1': 'Shaghelan1',
    'bikaran_1': 'Bikaran__1',
    'shaghela_1': 'Shaghela_1',
    'bikaran_2': 'Bikaran__2',
    'pop_malul_field': 'Pop_malul_',
    'pop_malul1': 'Pop_malul1',
    'pop_malu_1': 'Pop_malu_1',
    'masahat_ma': 'Masahat_ma',
    'tarakom_ja': 'Tarakom_ja',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'pop95_kol': 'Pop95_kol',
    'pop95_zan': 'Pop95_zan',
    'pop95_mard': 'Pop95_mard',
    'geom': 'MULTIPOLYGON',
}
mahalle_shp  = Path(__file__).resolve().parent / 'data' / 'mahalle' / 'mahalle.shp'

mantaghe_mapping = {
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'mantagheh': 'Mantagheh',
    'geom': 'MULTIPOLYGON',
}
mantaghe_shp  = Path(__file__).resolve().parent / 'data' / 'mantaghe' / 'mantaghe.shp'

brt_mapping = {
    'osm_id': 'osm_id',
    'code': 'code',
    'fclass': 'fclass',
    'name': 'name',
    'geom': 'MULTIPOINT',
}
brt_shp  = Path(__file__).resolve().parent / 'data' / 'brt' / 'brt.shp'

def run(verbose=True):
    # lm_transport = LayerMapping(Transport, transport_shp, transport_mapping, transform=False)
    # lm_transport.save(strict=True, verbose=verbose)
    # lm_bohran = LayerMapping(Bohran , bohran_shp, bohran_mapping, transform=False)
    # lm_bohran.save(strict=True, verbose=verbose)
    lm_bus =  LayerMapping(Bus , bus_shp, bus_mapping, transform=False)
    lm_bus.save(strict=True, verbose=verbose)
    lm_busline =  LayerMapping(Busline , busline_shp, busline_mapping, transform=False)
    lm_busline.save(strict=True, verbose=verbose)
    # lm_roads = LayerMapping(Roads , roads_shp , roads_mapping , transform=False)
    # lm_roads.save(strict=True , verbose=verbose)
    # lm_hospital= LayerMapping(Hospital, hospital_shp, hospital_mapping, transform=False)
    # lm_hospital.save(strict=True, verbose=verbose)
    # lm_fire = LayerMapping(Fire, fire_shp, fire_mapping, transform=False)
    # lm_fire.save(strict=True, verbose=verbose)
    # lm_police = LayerMapping(Police, police_shp, police_mapping, transform=False)
    # lm_police.save(strict=True, verbose=verbose)
    # lm_pharmacy = LayerMapping(Pharmacy, pharmacy_shp, pharmacy_mapping, transform=False)
    # lm_pharmacy.save(strict=True, verbose=verbose)
    # lm_school = LayerMapping(School, school_shp, school_mapping, transform=False)
    # lm_school.save(strict=True, verbose=verbose)
    # aludegi
    # lm_aludegi = LayerMapping(Aludegi, aludegi_shp, aludegi_mapping, transform=False)
    # lm_aludegi.save(strict=True, verbose=verbose)
    # trafic
    # lm_trafic = LayerMapping(Trafic, trafic_shp, trafic_mapping, transform=False)
    # lm_trafic.save(strict=True, verbose=verbose)
    #     busy
    # lm_busy = LayerMapping(Busy, busy_shp, busy_mapping, transform=False)
    # lm_busy.save(strict=True, verbose=verbose)
    #park
    # lm_park = LayerMapping(Park, park_shp, park_mapping, transform=False)
    # lm_park.save(strict=True, verbose=verbose)
    #pool
    # lm_pool = LayerMapping(Pool, pool_shp, pool_mapping, transform=False)
    # lm_pool.save(strict=True, verbose=verbose)
    #hotel
    # lm_hotel = LayerMapping(Hotel, hotel_shp, hotel_mapping, transform=False)
    # lm_hotel.save(strict=True, verbose=verbose)
    #zoo
    # lm_zoo = LayerMapping(Zoo, zoo_shp, zoo_mapping, transform=False)
    # lm_zoo.save(strict=True, verbose=verbose)
    #cng
    # lm_cng = LayerMapping(Cng, cng_shp, cng_mapping, transform=False)
    # lm_cng.save(strict=True, verbose=verbose)
    #shop
    # lm_shop= LayerMapping(Shop, shop_shp, shop_mapping, transform=False)
    # lm_shop.save(strict=True, verbose=verbose)
    #fuel
    # lm_fuel = LayerMapping(Fuel, fuel_shp, fuel_mapping, transform=False)
    # lm_fuel.save(strict=True, verbose=verbose)
    #gym
    # lm_gym = LayerMapping(Gym, gym_shp, gym_mapping, transform=False)
    # lm_gym.save(strict=True, verbose=verbose)
    #mahalle
    # lm_mahalle = LayerMapping(Mahalle, mahalle_shp, mahalle_mapping, transform=False)
    # lm_mahalle.save(strict=True, verbose=verbose)
    #mantaghe
    # lm_mantaghe = LayerMapping(Mantaghe, mantaghe_shp, mantaghe_mapping, transform=False)
    # lm_mantaghe.save(strict=True, verbose=verbose)
    # brt
    # lm_brt = LayerMapping(Brt, brt_shp, brt_mapping, transform=False)
    # lm_brt.save(strict=True, verbose=verbose)
    # brt_line()


def brt_line():
    brT = brt.objects.all()
    for item in brT:
        if '۱' in item.name and '۱۰' not in item.name :
            # print(item.name)
            item.line = '1'
            item.save()

    a = {
        '2' : '۲','3' : '۳','4' : '۴','5' : '۵','6' : '۷','7' : '۸','8' : '۹' , '9' : '۱۰',
    }
    for i in range(2 ,10,1 ):
        for item in brT:
            if a[str(i)] in item.name:
                # print(item.name)
                item.line = str(i)
                item.save()
            if 'دو' in item.name:
                item.line = '2'
                item.save()



    return 'done'

# TODO : rename layers
def geoserver_layer_add():
    trafic = LayerAdd(filename='trafic.shp' , filepath='trafic').shp_add()
    aludegi = LayerAdd(filename='aludegi.shp' , filepath='aludegi').shp_add()
