import cx_Oracle 
# from typing import Optional
# from fastapi import FastAPI , BackgroundTasks



# app = FastAPI()


class db_conn():
  def __init__(self , lat ,lon):
    self.lat = lat
    self.lon = lon
              
  def create_strings(self):
    my_dict = {
        "BRT" : f"SELECT   /*+ INDEX(c cola_spatial_idx) */  c.name, SDO_NN_DISTANCE(1) dist  FROM brt c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=3', 1) = 'TRUE' ORDER BY dist",
        "HOSPITAL" : f"SELECT   /*+ INDEX(c cola_spatial_idx) */  CONCAT(CONCAT(CONCAT(c.name, ' '), CONCAT(c.name_1, ' ')), CONCAT(c.name_12, ' ')), SDO_NN_DISTANCE(1) dist  FROM hospital c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=3', 1) = 'TRUE' ORDER BY dist",
        "FUEL" : f"SELECT  distinct /*+ INDEX(c cola_spatial_idx) */  c.name , SDO_NN_DISTANCE(1) dist  FROM fuel c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=3', 1) = 'TRUE' ORDER BY dist",
        "FIRE" : f"SELECT  distinct /*+ INDEX(c cola_spatial_idx) */  c.name , SDO_NN_DISTANCE(1) dist  FROM fire c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=1', 1) = 'TRUE' ORDER BY dist",
        "POLICE" : f"SELECT  distinct /*+ INDEX(c cola_spatial_idx) */  c.name , SDO_NN_DISTANCE(1) dist  FROM police c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=1', 1) = 'TRUE' ORDER BY dist",
        "PHARMACY" : f"SELECT  distinct /*+ INDEX(c cola_spatial_idx) */  c.name , SDO_NN_DISTANCE(1) dist  FROM pharmacy c   WHERE SDO_NN(c.geometry,  sdo_geometry(2001, 4326, sdo_point_type({self.lon}, {self.lat}, null), null, null), 'sdo_num_res=3', 1) = 'TRUE' ORDER BY dist",

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
               'name' : row[0],
               'dist' : row[1] 
           }
           counter = counter +1

        HOSPITAL = {}
        counter = 1
        for row in cursor.execute(self.create_strings()['HOSPITAL']) :
           HOSPITAL[str(counter)] ={
               'name' : row[0],
               'dist' : row[1] 
           }
           counter = counter + 1
        
        FUEL = {}
        counter = 1
        for row in cursor.execute(self.create_strings()['FUEL']) :
           FUEL[str(counter)] ={
               'name' : row[0],
               'dist' : row[1] 
           }
           counter = counter + 1
        
        FIRE = {}
        counter = 1
        for row in cursor.execute(self.create_strings()['FIRE']) :
           FIRE[str(counter)] ={
               'name' : row[0],
               'dist' : row[1] 
           }
           counter = counter + 1

        POLICE = {}
        counter = 1
        for row in cursor.execute(self.create_strings()['POLICE']) :
           POLICE[str(counter)] ={
               'name' : row[0],
               'dist' : row[1] 
           }
           counter = counter + 1

        PHARMACY = {}
        counter = 1
        for row in cursor.execute(self.create_strings()['PHARMACY']) :
           PHARMACY[str(counter)] ={
               'name' : row[0],
               'dist' : row[1] 
           }
           counter = counter + 1
        


        connection.commit()

        a= {"BRT" : BRT ,"HOSPITAL" : HOSPITAL ,"FUEL" : FUEL ,"FIRE" : FIRE ,"POLICE" : POLICE ,"PHARMACY" : PHARMACY}

        # print(type(a))

    return a

# a = db_conn(lat = '35.707664' , lon = '51.395552')
# print(a.conn())


# def main(lat , lon):
#     a = db_conn(lat = lat , lon = lon)
#     return a.conn()

# @app.get("/")
# def read_root(lat : str , lon : str ):
#     return main(lat=lat , lon=lon)