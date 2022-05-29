from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages
from django.contrib.auth.models import User
from . import tasks
from config.celery_conf import celery_app
# from client_oracle import db_conn
import json
from rest_framework.permissions import AllowAny  , IsAuthenticated
from .sql import PostConn
from rest_framework_simplejwt.backends import TokenBackend
from .models import Order , Park , Bohran
import random
from django.contrib.gis.geos import Point
import jwt
from django.conf import settings
import ast
from .load import brt_line
from django.core.serializers import serialize
# Create your views here.

def user_return(request):
    try:
        # take jwt token from request
        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]

        # take user from jwt token
        payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
        user = User.objects.get(id=payload['user_id'])
    except:
        return None

    return  user

# class Index(APIView):
#
#     permission_classes = [AllowAny]
#
#     def post(self, request):
#
#         user = user_return(request)
#         if not bool(user):
#             return Response(status=status.HTTP_401_UNAUTHORIZED)
#
#         # check if lat or lon is null
#         lat =request.data.get('lat')
#         lon = request.data.get('lon')
#
#         if str(lat) is None or str(lon) is None :
#             return Response({"status" : "400" , "message" : "lat or lon is none"})
#
#         lat = float(lat)
#         lon = float(lon)
#
#         #  make a order instance and register the order
#         order = Order()
#         try:
#             order.user = user
#         except:
#             pass
#         order.title = request.data.get('title')
#         order.id = random.getrandbits(52)
#         order.location = Point(lon , lat , srid=4326)
#         order.save()
#
#         # connect to postgres and take query results as a json
#         data = PostConn(lat,lon).pertrans()
#
#         return Response(data=data , headers={'Content-Type':'application/json','Access-Control-Allow-Origin':'http://localhost:3000','Access-Control-Allow-Credentials':True, 'Access-Control-Allow-Methods' : 'OPTIONS', 'Access-Control-Allow-Headers' : ['Origin', 'Content-Type', 'Accept']})


class PerTrans(APIView):
    permission_classes = [AllowAny]
    def post(self , request):

        user = user_return(request)
        if not bool(user):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        lat = request.data.get('lat')
        lon = request.data.get('lon')

        if str(lat) is None or str(lon) is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        lat = float(lat)
        lon = float(lon)

        data = PostConn(lat , lon).pertrans()
        return Response(data=data , status=status.HTTP_200_OK)

class PubTrans(APIView):
    permission_classes = [AllowAny]
    def post(self , request):

        user = user_return(request)
        if not bool(user):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        lat = request.data.get('lat')
        lon = request.data.get('lon')

        if lat is None or lon is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        lat = float(lat)
        lon = float(lon)

        data = PostConn(lat,lon).pubtrans()
        return Response(data=data , status=status.HTTP_200_OK)

class Refahi(APIView):
    permission_classes = [AllowAny]
    def post(self  , request):

        user = user_return(request)
        if not bool(user):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        lat = request.data.get('lat')
        lon = request.data.get('lon')

        if str(lat) is None or str(lon) is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        lat = float(lat)
        lon = float(lon)

        data = PostConn(lat , lon).refahi()
        return Response(data=data , status=status.HTTP_200_OK)

class Security(APIView):
    permission_classes = [AllowAny]
    def post(self , request):

        user = user_return(request)
        if not bool(user):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        lat = request.data.get('lat')
        lon = request.data.get('lon')

        if str(lat) is None or str(lon) is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        lat = float(lat)
        lon = float(lon)
        data = PostConn(lat, lon).security()
        return Response(data=data , status=status.HTTP_200_OK)
