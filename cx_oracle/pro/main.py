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
        "BRT" : f"SELECT   /*+ INDEX(c cola_spatial_idx) */  c.name, c.LINE , c.geometry.sdo_point.x longitude , c.geometry.sdo_point.y latitude ,  SDO_NN_DISTANCE(1) dist  FROM brt c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=3', 1) = 'TRUE' ORDER BY dist",
        "HOSPITAL" : f"SELECT   /*+ INDEX(c cola_spatial_idx) */  CONCAT(CONCAT(CONCAT(c.name, ' '), CONCAT(c.name_1, ' ')), CONCAT(c.name_12, ' ')), c.geometry.sdo_point.x longitude , c.geometry.sdo_point.y latitude ,  SDO_NN_DISTANCE(1) dist  FROM hospital c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=3', 1) = 'TRUE' ORDER BY dist",
        "FUEL" : f"SELECT  distinct /*+ INDEX(c cola_spatial_idx) */  c.name , c.geometry.sdo_point.x longitude , c.geometry.sdo_point.y latitude ,  SDO_NN_DISTANCE(1) dist  FROM fuel c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=3', 1) = 'TRUE' ORDER BY dist",
        "FIRE" : f"SELECT  distinct /*+ INDEX(c cola_spatial_idx) */  c.name , c.geometry.sdo_point.x longitude , c.geometry.sdo_point.y latitude ,  SDO_NN_DISTANCE(1) dist  FROM fire c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=1', 1) = 'TRUE' ORDER BY dist",
        "POLICE" : f"SELECT  distinct /*+ INDEX(c cola_spatial_idx) */  c.name , c.geometry.sdo_point.x longitude , c.geometry.sdo_point.y latitude ,  SDO_NN_DISTANCE(1) dist  FROM police c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=1', 1) = 'TRUE' ORDER BY dist",
        "PHARMACY" : f"SELECT  distinct /*+ INDEX(c cola_spatial_idx) */  c.name , c.geometry.sdo_point.x longitude , c.geometry.sdo_point.y latitude ,  SDO_NN_DISTANCE(1) dist  FROM pharmacy c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=3', 1) = 'TRUE' ORDER BY dist",
        "CNG" : f"SELECT   /*+ INDEX(c cola_spatial_idx) */  c.name , c.geometry.sdo_point.x longitude , c.geometry.sdo_point.y latitude ,    SDO_NN_DISTANCE(1) dist  FROM hospital c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=3', 1) = 'TRUE' ORDER BY dist",
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

        BRT = {}
        counter = 1
        for row in cursor.execute(self.create_strings()['BRT']) :
           BRT[str(counter)] ={
               "name" : row[0],
               "line" : row[1],
               "lon" : row[2],
               "lat" : row[3],
               "dist" : row[4] 
           }
           counter = counter +1

        HOSPITAL = {}
        counter = 1
        for row in cursor.execute(self.create_strings()['HOSPITAL']) :
           HOSPITAL[str(counter)] ={
               "name" : row[0],
               "dist" : row[1],
               "lon" : row[2],
               "lat" : row[3]
           }
           counter = counter + 1
        
        FUEL = {}
        counter = 1
        for row in cursor.execute(self.create_strings()['FUEL']) :
           FUEL[str(counter)] ={
               "name" : row[0],
               "dist" : row[1],
               "lon" : row[2],
               "lat" : row[3]
           }
           counter = counter + 1
        
        FIRE = {}
        counter = 1
        for row in cursor.execute(self.create_strings()['FIRE']) :
           FIRE[str(counter)] ={
               "name" : row[0],
               "dist" : row[1],
               "lon" : row[2],
               "lat" : row[3]
           }
           counter = counter + 1

        POLICE = {}
        counter = 1
        for row in cursor.execute(self.create_strings()['POLICE']) :
           POLICE[str(counter)] ={
               "name" : row[0],
               "dist" : row[1],
               "lon" : row[2],
               "lat" : row[3],
           }
           counter = counter + 1

        PHARMACY = {}
        counter = 1
        for row in cursor.execute(self.create_strings()['PHARMACY']) :
           PHARMACY[str(counter)] ={
               "name" : row[0],
               "dist" : row[1],
               "lon" : row[2],
               "lat" : row[3]
           }
           counter = counter + 1
        

        CNG = {}
        counter = 1
        for row in cursor.execute(self.create_strings()['CNG']) :
           CNG[str(counter)] ={
               "name" : row[0],
               "dist" : row[1],
               "lon" : row[2],
               "lat" : row[3]
           }
           counter = counter + 1

        GYM = {}
        counter = 1
        for row in cursor.execute(self.create_strings()['GYM']) :
           GYM[str(counter)] ={
               "name" : row[0],
               "dist" : row[1],
               "lon" : row[2],
               "lat" : row[3]
           }
           counter = counter + 1
        
        HOTEL = {}
        counter = 1
        for row in cursor.execute(self.create_strings()['HOTEL']) :
           HOTEL[str(counter)] ={
               "name" : row[0],
               "dist" : row[1],
               "lon" : row[2],
               "lat" : row[3],
           }
           counter = counter + 1
        
        PARK = {}
        counter = 1
        for row in cursor.execute(self.create_strings()['PARK']) :
           PARK[str(counter)] ={
               "name" : row[0],
               "dist" : row[1],
               "lon" : row[2],
               "lat" : row[3],
           }
           counter = counter + 1

        POOL = {}
        counter = 1
        for row in cursor.execute(self.create_strings()['POOL']) :
           POOL[str(counter)] ={
               "name" : row[0],
               "dist" : row[1],
               "lon" : row[2],
               "lat" : row[3],
           }
           counter = counter + 1


        SCHOOL = {}
        counter = 1
        for row in cursor.execute(self.create_strings()['SCHOOL']) :
           SCHOOL[str(counter)] ={
               "name" : row[0],
               "dist" : row[1],
               "lon" : row[2],
               "lat" : row[3],
           }
           counter = counter + 1


        SHOP = {}
        counter = 1
        for row in cursor.execute(self.create_strings()['SHOP']) :
           SHOP[str(counter)] ={
               "name" : row[0],
               "dist" : row[1],
               "lon" : row[2],
               "lat" : row[3],
           }
           counter = counter + 1

        ZOO = {}
        counter = 1
        for row in cursor.execute(self.create_strings()['ZOO']) :
           ZOO[str(counter)] ={
               "name" : row[0],
               "dist" : row[1],
               "lon" : row[2],
               "lat" : row[3],
           }
           counter = counter + 1

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

        TRAFIC = cursor.execute(self.create_strings()['TRAFIC'])
        TRAFIC = [row for row in TRAFIC][0][0]
        BUSY = cursor.execute(self.create_strings()['BUSY'])
        BUSY = [row for row in BUSY][0][0]
        


        connection.commit()

    return str(json.dumps({"status" : "200" , "BRT" : BRT ,"HOSPITAL" : HOSPITAL ,"FUEL" : FUEL ,"FIRE" : FIRE ,"POLICE" : POLICE ,"PHARMACY" : PHARMACY , "CNG" : CNG , "GYM" : GYM , "HOTEL" : HOTEL , "PARK" : PARK , "POOL" : POOL , "SCHOOL" : SCHOOL , "SHOP" : SHOP , "ZOO" : ZOO , "TRAFIC" : TRAFIC , "ALUDEGI" : ALUDEGI , "BUSY" : BUSY }))

# a = db_conn(lat = '35.707664' , lon = '51.395552')
# print(a.conn())


# def main(lat , lon):
#     a = db_conn(lat = lat , lon = lon)
#     return a.conn()

# @app.get("/")
# def read_root(lat : str , lon : str ):
#     return main(lat=lat , lon=lon)