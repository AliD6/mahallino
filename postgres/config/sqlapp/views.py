from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .sql import PostConn
# Create your views here.



class index(APIView):


    def post(self , request):

        lat = request.data.get('lat')
        lon = request.data.get('lon')

        
        Post = PostConn(lat,lon).db_conn()

        # taxi  = serializers.serialize("json" ,Transport.objects.annotate(distance=Distance('point',pnt )))
        # taxi = Transport.objects.filter(geom__distance_lt=(pnt , m==5 ))
        



        return Response(Post)