from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages
from django.contrib.auth.models import User
from . import tasks
from config.celery_conf import celery_app
from client_oracle import db_conn
import json
from rest_framework.permissions import AllowAny  , IsAuthenticated
from .sql import PostConn
from rest_framework_simplejwt.backends import TokenBackend
from .models import Order
import random
from django.contrib.gis.geos import Point
import jwt
from django.conf import settings
# Create your views here.


class index(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        print('=='*50)
        print('this')

        try:

            # take jwt token from request
            token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        
            # take user from jwt token
            payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
        except:
            pass

        print('data' , request.data)
        # check if lat or lon is null 
        lat =float(request.data.get('lat'))
        lon = float(request.data.get('lon'))
        print('lat' ,type(lat))
        print('lon' , type(lon))
        if str(lat) is None or str(lon) is None :
            return Response({"status" : "400" , "message" : "lat or lon is none"})


        #  make a order instance and register the order
        order = Order()
        try:
            order.user = user
        except:
            pass
        order.title = request.data.get('title')
        order.id = random.getrandbits(52)
        order.location = Point(lon , lat , srid=4326)
        order.save()

        
        
       
        # connect to oracle and take query results as a json
        oracle_conn = db_conn()
        oracle_data = oracle_conn.call( str(lat) + ',' + str(lon))
        oracle_data = oracle_data

        # connect to postgres and take query results as a json
        Post = PostConn(lat,lon).db_conn()


        # concat two jsons
        data = {**oracle_data , **Post}

        return Response(data , headers={'Content-Type':'application/json','Access-Control-Allow-Origin':'http://localhost:3000','Access-Control-Allow-Credentials':True, 'Access-Control-Allow-Methods' : 'OPTIONS', 'Access-Control-Allow-Headers' : ['Origin', 'Content-Type', 'Accept']})

    def get(self , request):

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)