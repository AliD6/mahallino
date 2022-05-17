import cx_Oracle 
# from typing import Optional
# from fastapi import FastAPI , BackgroundTasks
import json



# app = FastAPI()


class db_conn():
  def __init__(self , lat ,lon):
    self.lat = lat
    self.lon = lon
              
  def create_strings(self):
    my_dict = {
        "BRT" : f"SELECT   /*+ INDEX(c cola_spatial_idx) */  c.name, c.LINE , c.geometry.sdo_point.x longitude , c.geometry.sdo_point.y latitude ,  SDO_NN_DISTANCE(1) dist  FROM br c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=3', 1) = 'TRUE' ORDER BY dist",
        "HOSPITAL" : f"SELECT   /*+ INDEX(c cola_spatial_idx) */  CONCAT(CONCAT(CONCAT(c.name, ' '), CONCAT(c.name_1, ' ')), CONCAT(c.name_12, ' ')), c.geometry.sdo_point.x longitude , c.geometry.sdo_point.y latitude ,  SDO_NN_DISTANCE(1) dist  FROM hospital c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=3', 1) = 'TRUE' ORDER BY dist",
        "FUEL" : f"SELECT  distinct /*+ INDEX(c cola_spatial_idx) */  c.name , c.geometry.sdo_point.x longitude , c.geometry.sdo_point.y latitude ,  SDO_NN_DISTANCE(1) dist  FROM fuel c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=3', 1) = 'TRUE' ORDER BY dist",
        "FIRE" : f"SELECT  distinct /*+ INDEX(c cola_spatial_idx) */  c.name , c.geometry.sdo_point.x longitude , c.geometry.sdo_point.y latitude ,  SDO_NN_DISTANCE(1) dist  FROM fire c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=1', 1) = 'TRUE' ORDER BY dist",
        "POLICE" : f"SELECT  distinct /*+ INDEX(c cola_spatial_idx) */  c.name , c.geometry.sdo_point.x longitude , c.geometry.sdo_point.y latitude ,  SDO_NN_DISTANCE(1) dist  FROM police c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=1', 1) = 'TRUE' ORDER BY dist",
        "PHARMACY" : f"SELECT  distinct /*+ INDEX(c cola_spatial_idx) */  c.name , c.geometry.sdo_point.x longitude , c.geometry.sdo_point.y latitude ,  SDO_NN_DISTANCE(1) dist  FROM pharmacy c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=3', 1) = 'TRUE' ORDER BY dist",
        "CNG" : f"SELECT   /*+ INDEX(c cola_spatial_idx) */  c.name , c.geometry.sdo_point.x longitude , c.geometry.sdo_point.y latitude ,    SDO_NN_DISTANCE(1) dist  FROM cng c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=3', 1) = 'TRUE' ORDER BY dist",
        "GYM" : f"SELECT   /*+ INDEX(c cola_spatial_idx) */  c.name , c.geometry.sdo_point.x longitude , c.geometry.sdo_point.y latitude ,   SDO_NN_DISTANCE(1) dist  FROM gym c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=3', 1) = 'TRUE' ORDER BY dist",
        "HOTEL" : f"SELECT   /*+ INDEX(c cola_spatial_idx) */  c.name , c.geometry.sdo_point.x longitude , c.geometry.sdo_point.y latitude ,    SDO_NN_DISTANCE(1) dist  FROM hotel c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=3', 1) = 'TRUE' ORDER BY dist",
        "PARK" : f"SELECT   /*+ INDEX(c cola_spatial_idx) */  c.name , c.geometry.sdo_point.x longitude , c.geometry.sdo_point.y latitude ,   SDO_NN_DISTANCE(1) dist  FROM park c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=3', 1) = 'TRUE' ORDER BY dist",
        "POOL" : f"SELECT   /*+ INDEX(c cola_spatial_idx) */  c.name , c.geometry.sdo_point.x longitude , c.geometry.sdo_point.y latitude ,    SDO_NN_DISTANCE(1) dist  FROM pool c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=3', 1) = 'TRUE' ORDER BY dist",
        "SCHOOL" : f"SELECT distinct  /*+ INDEX(c cola_spatial_idx) */  c.name , c.geometry.sdo_point.x longitude , c.geometry.sdo_point.y latitude ,   SDO_NN_DISTANCE(1) dist  FROM school c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=5', 1) = 'TRUE' ORDER BY dist",
        "SHOP" : f"SELECT   /*+ INDEX(c cola_spatial_idx) */  c.name ,  c.geometry.sdo_point.x longitude , c.geometry.sdo_point.y latitude ,   SDO_NN_DISTANCE(1) dist  FROM shop c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=3', 1) = 'TRUE' ORDER BY dist",
        "ZOO" : f"SELECT   /*+ INDEX(c cola_spatial_idx) */  c.name ,  c.geometry.sdo_point.x longitude , c.geometry.sdo_point.y latitude ,   SDO_NN_DISTANCE(1) dist  FROM zoo c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=1', 1) = 'TRUE' ORDER BY dist",
        "MANTAGHE" : f"SELECT m.mantagheh FROM mantaghe m WHERE SDO_CONTAINS( m.geometry,SDO_GEOMETRY (2001, 4326, SDO_POINT_TYPE({self.lon},{self.lat}, null),Null, Null)) = 'TRUE'",
        "MAHALLE" : f"SELECT m.mahale_nam FROM mahalle m WHERE SDO_CONTAINS(m.geometry,SDO_GEOMETRY(2001, 4326, SDO_POINT_TYPE({self.lon},{self.lat}, null),Null, Null)) = 'TRUE'",
        "ALUDEGI" : f"select SDO_CONTAINS( m.geometry,SDO_GEOMETRY (2001, 4326, SDO_POINT_TYPE({self.lon},{self.lat}, null),Null, Null)) from aludegi m",
        "TRAFIC" : f"select SDO_CONTAINS( m.geometry,SDO_GEOMETRY (2001, 4326, SDO_POINT_TYPE({self.lon},{self.lat}, null),Null, Null)) from trafic m",
        "BUSY" : f"select count(*) from busy h where  sdo_geom.sdo_distance(  sdo_geometry(2001, 4326, sdo_point_type({self.lon},{self.lat}, null), null, null),  h.geometry,  0.01,  'unit=M' ) < 1000",
        # "HIGH" : f"SELECT   /*+ INDEX(c cola_spatial_idx) */  c.name,  SDO_NN_DISTANCE(1) dist  FROM high c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon},{self.lat}, null), null, null), 'sdo_num_res=3', 1) = 'TRUE' ORDER BY dist"
        # in this part query strings will be completed
    }
    return my_dict

  def conn(self):
    with cx_Oracle.connect(user = 'SEDREH_USER' , password = '20672067ali' , dsn = 'localhost/orcl' , encoding = 'UTF-8') as connection:
        cursor = connection.cursor()

        data = []

        # BRT = {}
        # counter = 1
        # for row in cursor.execute(self.create_strings()['BRT']) :
        #    BRT[str(counter)] ={
        #        "name" : row[0],
        #        "line" : row[1],
        #        "lon" : row[2],
        #        "lat" : row[3],
        #        "dist" : row[4] 
        #    }
        #    counter = counter +1
        brt = []
        for row in cursor.execute(self.create_strings()['BRT']) :
            brt.append({"name" : row[0] , "dist" : row[3] , "lon" : row[1] , "lat" : row[2]})
        BRT = {"title" : "BRT" , "id" : 302 , "value" : brt}

        # print(BRT)

        data.append(BRT)

        hospital = []
        for row in cursor.execute(self.create_strings()['HOSPITAL']) :
            hospital.append({"name" : row[0] , "dist" : row[3] , "lon" : row[1] , "lat" : row[2]})
        HOSPITAL = {"title" : "HOSPITAL" , "id" : 503 , "value" : hospital}

        data.append(HOSPITAL)

        # HOSPITAL = {}
        # counter = 1
        # for row in cursor.execute(self.create_strings()['HOSPITAL']) :
        #    HOSPITAL[str(counter)] ={
        #        "name" : row[0],
        #        "dist" : row[1],
        #        "lon" : row[2],
        #        "lat" : row[3]
        #    }
        #    counter = counter + 1
        
        fuel = []
        for row in cursor.execute(self.create_strings()['FUEL']) :
            fuel.append({"name" : row[0] , "dist" : row[3] , "lon" : row[1] , "lat" : row[2]})
        FUEL = {"title" : "FUEL" , "id" : 204 , "value" : fuel}

        data.append(FUEL)

        # FUEL = {}
        # counter = 1
        # for row in cursor.execute(self.create_strings()['FUEL']) :
        #    FUEL[str(counter)] ={
        #        "name" : row[0],
        #        "dist" : row[1],
        #        "lon" : row[2],
        #        "lat" : row[3]
        #    }
        #    counter = counter + 1

        fire = []
        for row in cursor.execute(self.create_strings()['FIRE']) :
            fire.append({"name" : row[0] , "dist" : row[3] , "lon" : row[1] , "lat" : row[2]})
        FIRE = {"title" : "FIRE" , "id" : 502 , "value" : fire}
        
        data.append(FIRE)

        # FIRE = {}
        # counter = 1
        # for row in cursor.execute(self.create_strings()['FIRE']) :
        #    FIRE[str(counter)] ={
        #        "name" : row[0],
        #        "dist" : row[1],
        #        "lon" : row[2],
        #        "lat" : row[3]
        #    }
        #    counter = counter + 1

        police = []
        for row in cursor.execute(self.create_strings()['POLICE']) :
            police.append({"name" : row[0] , "dist" : row[3] , "lon" : row[1] , "lat" : row[2]})
        POLICE = {"title" : "POLICE" , "id" : 501 , "value" : police}

        data.append(POLICE)

        # POLICE = {}
        # counter = 1
        # for row in cursor.execute(self.create_strings()['POLICE']) :
        #    POLICE[str(counter)] ={
        #        "name" : row[0],
        #        "dist" : row[1],
        #        "lon" : row[2],
        #        "lat" : row[3],
        #    }
        #    counter = counter + 1

        pharmacy = []
        for row in cursor.execute(self.create_strings()['PHARMACY']) :
            pharmacy.append({"name" : row[0] , "dist" : row[3] , "lon" : row[1] , "lat" : row[2]})
        PHARMACY = {"title" : "PHARMACY" , "id" : 404 , "value" : pharmacy}

        data.append(PHARMACY)

        # PHARMACY = {}
        # counter = 1
        # for row in cursor.execute(self.create_strings()['PHARMACY']) :
        #    PHARMACY[str(counter)] ={
        #        "name" : row[0],
        #        "dist" : row[1],
        #        "lon" : row[2],
        #        "lat" : row[3]
        #    }
        #    counter = counter + 1
        

        cng = []
        for row in cursor.execute(self.create_strings()['CNG']) :
            cng.append({"name" : row[0] , "dist" : row[3] , "lon" : row[1] , "lat" : row[2]})
        CNG = {"title" : "CNG" , "id" : 205 , "value" : cng}

        data.append(CNG)

        # CNG = {}
        # counter = 1
        # for row in cursor.execute(self.create_strings()['CNG']) :
        #    CNG[str(counter)] ={
        #        "name" : row[0],
        #        "dist" : row[1],
        #        "lon" : row[2],
        #        "lat" : row[3]
        #    }
        #    counter = counter + 1

        gym = []
        for row in cursor.execute(self.create_strings()['GYM']) :
            gym.append({"name" : row[0] , "dist" : row[3] , "lon" : row[1] , "lat" : row[2]})
        GYM = {"title" : "GYM" , "id" : 405 , "value" : gym}

        data.append(GYM)

        # GYM = {}
        # counter = 1
        # for row in cursor.execute(self.create_strings()['GYM']) :
        #    GYM[str(counter)] ={
        #        "name" : row[0],
        #        "dist" : row[1],
        #        "lon" : row[2],
        #        "lat" : row[3]
        #    }
        #    counter = counter + 1
        
        hotel = []
        for row in cursor.execute(self.create_strings()['HOTEL']) :
            hotel.append({"name" : row[0] , "dist" : row[3] , "lon" : row[1] , "lat" : row[2]})
        HOTEL = {"title" : "HOTEL" , "id" : 409 , "value" : hotel}

        data.append(HOTEL)

        # HOTEL = {}
        # counter = 1
        # for row in cursor.execute(self.create_strings()['HOTEL']) :
        #    HOTEL[str(counter)] ={
        #        "name" : row[0],
        #        "dist" : row[1],
        #        "lon" : row[2],
        #        "lat" : row[3],
        #    }
        #    counter = counter + 1
        
        park = []
        for row in cursor.execute(self.create_strings()['PARK']) :
            park.append({"name" : row[0] , "dist" : row[3] , "lon" : row[1] , "lat" : row[2]})
        PARK = {"title" : "PARK" , "id" : 403 , "value" : park}

        data.append(PARK)

        # PARK = {}
        # counter = 1
        # for row in cursor.execute(self.create_strings()['PARK']) :
        #    PARK[str(counter)] ={
        #        "name" : row[0],
        #        "dist" : row[1],
        #        "lon" : row[2],
        #        "lat" : row[3],
        #    }
        #    counter = counter + 1

        pool = []
        for row in cursor.execute(self.create_strings()['POOL']) :
            pool.append({"name" : row[0] , "dist" : row[3] , "lon" : row[1] , "lat" : row[2]})
        POOL = {"title" : "POOL" , "id" : 406 , "value" : pool}
        data.append(POOL)
        # POOL = {}
        # counter = 1
        # for row in cursor.execute(self.create_strings()['POOL']) :
        #    POOL[str(counter)] ={
        #        "name" : row[0],
        #        "dist" : row[1],
        #        "lon" : row[2],
        #        "lat" : row[3],
        #    }
        #    counter = counter + 1

        school = []
        for row in cursor.execute(self.create_strings()['SCHOOL']) :
            school.append({"name" : row[0] , "dist" : row[3] , "lon" : row[1] , "lat" : row[2]})
        SCHOOL = {"title" : "SCHOOL" , "id" : 401 , "value" : school}
        data.append(SCHOOL)

        # SCHOOL = {}
        # counter = 1
        # for row in cursor.execute(self.create_strings()['SCHOOL']) :
        #    SCHOOL[str(counter)] ={
        #        "name" : row[0],
        #        "dist" : row[1],
        #        "lon" : row[2],
        #        "lat" : row[3],
        #    }
        #    counter = counter + 1


        shop = []
        for row in cursor.execute(self.create_strings()['SHOP']) :
            shop.append({"name" : row[0] , "dist" : row[3] , "lon" : row[1] , "lat" : row[2]})
        SHOP = {"title" : "SHOP" , "id" : 407 , "value" : shop}
        data.append(SHOP)
        # SHOP = {}
        # counter = 1
        # for row in cursor.execute(self.create_strings()['SHOP']) :
        #    SHOP[str(counter)] ={
        #        "name" : row[0],
        #        "dist" : row[1],
        #        "lon" : row[2],
        #        "lat" : row[3],
        #    }
        #    counter = counter + 1

        zoo = []
        for row in cursor.execute(self.create_strings()['ZOO']) :
            zoo.append({"name" : row[0] , "dist" : row[3] , "lon" : row[1] , "lat" : row[2]})
        ZOO = {"title" : "ZOO" , "id" : 410 , "value" : zoo}
        data.append(ZOO)
        # ZOO = {}
        # counter = 1
        # for row in cursor.execute(self.create_strings()['ZOO']) :
        #    ZOO[str(counter)] ={
        #        "name" : row[0],
        #        "dist" : row[1],
        #        "lon" : row[2],
        #        "lat" : row[3],
        #    }
        #    counter = counter + 1

        # HIGH = {}
        # counter = 1
        # for row in cursor.execute(self.create_strings()['HIGH']) :
        #     HIGH[str(counter)] ={
        #        "name" : row[0],
        #        "dist" : row[1],
        #        }
        #     counter = counter + 1

        ALUDEGI = cursor.execute(self.create_strings()['ALUDEGI'])
        ALUDEGI = [row for row in ALUDEGI][0][0]
        # print(ALUDEGI)

        TRAFIC = cursor.execute(self.create_strings()['TRAFIC'])
        TRAFIC = [row for row in TRAFIC][0][0]

        tarh = []
        # for row in cursor.execute(self.create_strings()['ZOO']) :
        tarh.append({"name" : "زوج و فرد" , "state" : True if TRAFIC == 'TRUE' else False })
        tarh.append({"name" : "آلودگی هوا" , "state" : True if TRAFIC == 'TRUE' else False })
        TARH = {"title" : "TARH" , "id" : 203 , "value" : tarh}
        data.append(TARH)

        BUSY = cursor.execute(self.create_strings()['BUSY'])
        # BUSY = [row for row in BUSY][0][0]
        terafic = {"title" : "terafic" , "id" : 201 , "value" : [row for row in BUSY][0][0] }
        data.append(terafic)


        connection.commit()
    return str(data)
    # return str(json.dumps({"status" : "200" , "BRT" : BRT ,"HOSPITAL" : HOSPITAL ,"FUEL" : FUEL ,"FIRE" : FIRE ,"POLICE" : POLICE ,"PHARMACY" : PHARMACY , "CNG" : CNG , "GYM" : GYM , "HOTEL" : HOTEL , "PARK" : PARK , "POOL" : POOL , "SCHOOL" : SCHOOL , "SHOP" : SHOP , "ZOO" : ZOO , "TARH" : TARH ,  "terafic" : terafic }))

# a = db_conn(lat = '35.707664' , lon = '51.395552')
# a.conn()


# def main(lat , lon):
#     a = db_conn(lat = lat , lon = lon)
#     return a.conn()

# @app.get("/")
# def read_root(lat : str , lon : str ):
#     return main(lat=lat , lon=lon)