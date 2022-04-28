from .models import Transport , Bohran , Bus , Busline
from django.contrib.gis.utils import LayerMapping
from pathlib import Path


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

def run(verbose=True):
    # lm_transport = LayerMapping(Transport, transport_shp, transport_mapping, transform=False)
    # lm_transport.save(strict=True, verbose=verbose)
    # lm_bohran = LayerMapping(Bohran , bohran_shp, bohran_mapping, transform=False)
    # lm_bohran.save(strict=True, verbose=verbose)
    # lm_bus =  LayerMapping(Bus , bus_shp, bus_mapping, transform=False)
    # lm_bus.save(strict=True, verbose=verbose)
    lm_busline =  LayerMapping(Busline , busline_shp, busline_mapping, transform=False)
    lm_busline.save(strict=True, verbose=verbose)




